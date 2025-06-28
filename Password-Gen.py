import hashlib
import random
import string

def generate_site_code(site_name):
    """Генерация случайного кода сайта (на его названии)"""
    site_name = site_name.lower().replace(" ", "")
    if not site_name:
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(4))
    # Выбираем 4 случайных символа из site_name
    available_chars = list(site_name)
    if len(available_chars) < 4:
        available_chars.extend(['X'] * (4 - len(available_chars)))
    selected_chars = random.sample(available_chars, 4)
    # Перемешиваем для дополнительной вариативности
    random.shuffle(selected_chars)
    return ''.join(selected_chars).upper()

def generate_random_code(importance):
    """Генерация случайного кода по важности (5-16 символов)"""
    length_map = {5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16}  # Низкая, средняя, высокая важность
    length = length_map.get(importance, 10)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_domain_index(domain):
    """Генерация случайного индекса домена (на основе названия)"""
    domain = domain.lower().replace(".", "")
    if not domain:
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(random.randint(3, 4)))
    # Выбираем 3-4 случайных символа из domain
    available_chars = list(domain)
    length = random.randint(3, 4)
    if len(available_chars) < length:
        available_chars.extend(['X'] * (length - len(available_chars)))
    selected_chars = random.sample(available_chars, length)
    # Перемешиваем для дополнительной вариативности
    random.shuffle(selected_chars)
    return ''.join(selected_chars).upper()

def generate_special_char():
    """Генерация случайного символа (используйте если подходит)"""
    special_chars = "!@#$%^&*"
    return random.choice(special_chars)

def generate_password(site_name, domain, importance=2, version=0):
    """Генерация пароля"""
    site_code = generate_site_code(site_name)
    random_code = generate_random_code(importance)
    domain_index = generate_domain_index(domain)
    version_code = f"V{version}"
    special_char = generate_special_char()
    return f"{site_code}-{random_code}-{domain_index}-{version_code}-{special_char}"

# Примеры использования
if __name__ == "__main__":
    print(generate_password("", "", importance=10, version=0))
    print(generate_password("", "", importance=10, version=0))
    print(generate_password("", "", importance=10, version=0))
    print(generate_password("", "", importance=10, version=0))
    print(generate_password("", "", importance=10, version=0))