import secrets
import string
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

# === Вспомогательные функции ===
def type_print(text, delay=0.02, color=Fore.GREEN):
    """Вывод с эффектом печати"""
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def input_prompt(prompt, color=Fore.CYAN):
    """Ввод с цветом"""
    return input(color + prompt + Style.RESET_ALL).strip()

# === Логика генератора ===
def generate_site_code(project_index):
    characters = string.ascii_uppercase + string.digits
    if not project_index:
        return ''.join(secrets.choice(characters) for _ in range(4))
    cleaned = ''.join(ch for ch in project_index.upper() if ch.isalnum())
    while len(cleaned) < 4:
        cleaned += secrets.choice(characters)
    return cleaned[:4]

def generate_project_name_code(project_name):
    characters = string.ascii_uppercase + string.digits
    if not project_name:
        return ''.join(secrets.choice(characters) for _ in range(secrets.choice([3, 4])))
    cleaned = ''.join(ch for ch in project_name.upper() if ch.isalnum())
    length = secrets.choice([3, 4])
    while len(cleaned) < length:
        cleaned += secrets.choice(characters)
    return cleaned[:length]

def generate_random_code(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_password(project_index, project_name, length, version):
    site_code = generate_site_code(project_index)
    name_code = generate_project_name_code(project_name)
    random_code = generate_random_code(length)
    version_code = f"V{version}"
    parts = [site_code, random_code, name_code, version_code]
    secrets.SystemRandom().shuffle(parts)
    return '-'.join(parts)

# === Основная программа ===
if __name__ == "__main__":
    type_print("=== SECURE PASSWORD GENERATOR v2 ===", 0.01, Fore.YELLOW)
    type_print("Запуск утилиты...", 0.02, Fore.YELLOW)
    print()

    project_index = input_prompt("Индекс проекта?: ")
    project_name = input_prompt("Именование проекта?: ")

    while True:
        try:
            length = int(input_prompt("Сложность пароля? (от 5 до 25): "))
            if 5 <= length <= 25:
                break
            type_print("Ошибка: введите число от 5 до 25.", 0.01, Fore.RED)
        except ValueError:
            type_print("Ошибка: введите число.", 0.01, Fore.RED)

    while True:
        try:
            version = int(input_prompt("Версия пароля? (от 0): "))
            if version >= 0:
                break
            type_print("Ошибка: введите целое число >= 0.", 0.01, Fore.RED)
        except ValueError:
            type_print("Ошибка: введите число.", 0.01, Fore.RED)

    type_print("\nГенерация пароля...", 0.02, Fore.YELLOW)
    password = generate_password(project_index, project_name, length, version)

    print(Fore.GREEN + "\n================= СГЕНЕРИРОВАННЫЙ ПАРОЛЬ =================")
    print(Fore.WHITE + Style.BRIGHT + password)
    print(Fore.GREEN + "==========================================================")
