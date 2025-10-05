import pygame
import secrets
import string
import pyperclip

pygame.init()

# --- Константы ---
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 28
FONT = pygame.font.SysFont("consolas", FONT_SIZE)
TITLE_FONT = pygame.font.SysFont("consolas", 40, bold=True)
BG_COLOR = (0, 0, 0)
TEXT_COLOR = (0, 255, 0)
BTN_COLOR = (50, 50, 50)
BTN_HOVER = (80, 80, 80)

# --- Интерфейсные тексты ---
TEXTS = {
    "rus": {
        "logo": "Password-Gen V3",
        "lang_choice": "Выберите язык: 1 - Русский, 2 - English",
        "index": "Индекс проекта?:",
        "name": "Именование проекта?:",
        "length": "Длина основной части пароля (5-25):",
        "version": "Версия пароля?:",
        "result": "Сгенерированный пароль:",
        "copy": "Copy",
        "copied": "Пароль скопирован!"
    },
    "eng": {
        "logo": "Password-Gen V3",
        "lang_choice": "Select language: 1 - Русский, 2 - English",
        "index": "Project index?:",
        "name": "Project name?:",
        "length": "Password main part length (5-25):",
        "version": "Password version?:",
        "result": "Generated password:",
        "copy": "Copy",
        "copied": "Password copied!"
    }
}


# --- Генератор ---
def leet_transform(text):
    mapping = {"A": "4", "S": "$", "E": "3", "O": "0", "I": "1", "T": "7"}
    return ''.join(mapping.get(ch, ch) for ch in text.upper())


def generate_password(project_index, project_name, length, version):
    # Преобразованные коды
    site_code = leet_transform(project_index)[:4] if project_index else ''
    name_code = leet_transform(project_name)[:4] if project_name else ''

    # Основная случайная часть
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
    random_code = ''.join(secrets.choice(chars) for _ in range(length))

    version_code = f"V{version}"
    parts = [site_code, name_code, random_code, version_code]
    parts = [p for p in parts if p]  # Убираем пустые
    secrets.SystemRandom().shuffle(parts)
    return '-'.join(parts)


# --- Ввод текста ---
def text_input(screen, prompt, lang):
    user_text = ""
    while True:
        screen.fill(BG_COLOR)
        # Заголовок
        title_surface = TITLE_FONT.render(TEXTS[lang]["logo"], True, TEXT_COLOR)
        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 20))

        # Промпт
        prompt_surface = FONT.render(prompt, True, TEXT_COLOR)
        screen.blit(prompt_surface, (50, HEIGHT // 2 - 40))

        # Ввод
        input_surface = FONT.render(user_text, True, TEXT_COLOR)
        screen.blit(input_surface, (50, HEIGHT // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_text
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit();
                    exit()
                else:
                    if len(user_text) < 30:
                        user_text += event.unicode


# --- Кнопка ---
def draw_button(screen, text, x, y, w, h, mouse_pos):
    rect = pygame.Rect(x, y, w, h)
    color = BTN_HOVER if rect.collidepoint(mouse_pos) else BTN_COLOR
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, TEXT_COLOR, rect, 2)
    txt_surface = FONT.render(text, True, TEXT_COLOR)
    screen.blit(txt_surface, (x + w // 2 - txt_surface.get_width() // 2,
                              y + h // 2 - txt_surface.get_height() // 2))
    return rect


# --- Главный цикл ---
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Password-Gen V3")
    clock = pygame.time.Clock()

    # Выбор языка
    lang = "rus"
    while True:
        screen.fill(BG_COLOR)
        title_surface = TITLE_FONT.render(TEXTS[lang]["logo"], True, TEXT_COLOR)
        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 200))

        choice_surface = FONT.render(TEXTS[lang]["lang_choice"], True, TEXT_COLOR)
        screen.blit(choice_surface, (WIDTH // 2 - choice_surface.get_width() // 2, 300))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    lang = "rus";
                    break
                elif event.key == pygame.K_2:
                    lang = "eng";
                    break
        else:
            continue
        break

    # Ввод данных
    project_index = text_input(screen, TEXTS[lang]["index"], lang)
    project_name = text_input(screen, TEXTS[lang]["name"], lang)

    while True:
        try:
            length = int(text_input(screen, TEXTS[lang]["length"], lang))
            if 5 <= length <= 25:
                break
        except ValueError:
            pass

    while True:
        try:
            version = int(text_input(screen, TEXTS[lang]["version"], lang))
            if version >= 0:
                break
        except ValueError:
            pass

    # Генерация пароля
    password = generate_password(project_index, project_name, length, version)

    # Результат
    copied = False
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(BG_COLOR)

        # Лого
        title_surface = TITLE_FONT.render(TEXTS[lang]["logo"], True, TEXT_COLOR)
        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 50))

        # Пароль
        result_surface = FONT.render(f"{TEXTS[lang]['result']} {password}", True, TEXT_COLOR)
        screen.blit(result_surface, (50, HEIGHT // 2))

        # Кнопка Copy
        btn_rect = draw_button(screen, TEXTS[lang]["copy"], WIDTH // 2 - 60, HEIGHT // 2 + 50, 120, 40, mouse_pos)

        if copied:
            copied_surface = FONT.render(TEXTS[lang]["copied"], True, TEXT_COLOR)
            screen.blit(copied_surface, (WIDTH // 2 - copied_surface.get_width() // 2, HEIGHT // 2 + 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_rect.collidepoint(mouse_pos):
                    pyperclip.copy(password)
                    copied = True

        clock.tick(30)


if __name__ == "__main__":
    main()
