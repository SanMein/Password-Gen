import hashlib
import random
import string


# Шаблон 1: Хэшированный префикс + случайный суффикс
def template1(site_name, domain, importance=2, version=0):
    length = max(5, min(importance, 12)) + 4
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    hash_input = (site_name.lower() + domain.lower() + str(version)).encode()
    prefix = hashlib.sha256(hash_input).hexdigest()[:6].upper()
    suffix = ''.join(random.choice(characters) for _ in range(length))
    return f"{prefix}{suffix}"


# Шаблон 2: Чередование символов сайта и домена
def template2(site_name, domain, importance=2, version=0):
    site_chars = list(site_name.lower().replace(" ", ""))
    domain_chars = list(domain.lower().replace(".", ""))
    length = max(5, min(importance, 10))
    characters = string.ascii_letters + string.digits
    random_part = ''.join(random.choice(characters) for _ in range(length))
    result = ""
    max_len = min(max(len(site_chars), len(domain_chars)), 5)
    for i in range(max_len):
        if i < len(site_chars):
            result += site_chars[i].upper()
        if i < len(domain_chars):
            result += domain_chars[i].upper()
        result += random.choice(".-|")
    return f"{result}{random_part}V{version}"


# Шаблон 3: Буквенно-цифровой микс с версионным суффиксом
def template3(site_name, domain, importance=2, version=0):
    site_chars = list(site_name.lower().replace(" ", ""))
    domain_chars = list(domain.lower().replace(".", ""))
    length = max(6, min(importance, 14))
    chars = string.ascii_letters + string.digits
    result = []
    for _ in range(length // 2):
        if site_chars:
            result.append(random.choice(site_chars).upper())
        else:
            result.append(random.choice(string.ascii_uppercase))
        if domain_chars:
            result.append(random.choice(domain_chars).upper())
        else:
            result.append(random.choice(string.ascii_uppercase))
    numeric_code = ''.join(random.choice(string.digits) for _ in range(4))
    special = random.choice("!@#$%")
    return f"{''.join(result)}{numeric_code}V{version}{special}"


# Шаблон 4: Хэш-основа с сегментацией
def template4(site_name, domain, importance=2, version=0):
    hash_input = (site_name.lower() + domain.lower() + str(version)).encode()
    hash_str = hashlib.md5(hash_input).hexdigest()[:12]
    segments = [hash_str[i:i + 3] for i in range(0, 12, 3)]
    length = max(3, min(importance // 2, 6))
    random_part = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    special = random.choice("!@#$%^&*")
    return f"{segments[0].upper()}-{random_part}-{segments[1].upper()}V{version}{special}"


# Шаблон 5: Символьная матрица
def template5(site_name, domain, importance=2, version=0):
    site_part = ''.join(random.sample(list(site_name.lower().replace(" ", "") + "X" * 4)[:4], 4)).upper()
    domain_part = ''.join(random.sample(list(domain.lower().replace(".", "") + "X" * 4)[:4], 4)).upper()
    length = max(4, min(importance, 8))
    random_part = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    special_chars = ''.join(random.choice("!@#$%^&*") for _ in range(2))
    return f"{site_part[0:2]}{random_part[0:2]}{domain_part[0:2]}{special_chars}{version}{site_part[2:4]}{random_part[2:]}"


# Шаблон 6: Кодированный числовой блок
def template6(site_name, domain, importance=2, version=0):
    hash_input = (site_name.lower() + domain.lower()).encode()
    numeric_code = str(int(hashlib.sha256(hash_input).hexdigest(), 16))[-6:]
    length = max(4, min(importance, 10))
    chars = string.ascii_letters
    prefix = ''.join(random.choice(chars) for _ in range(length // 2))
    suffix = ''.join(random.choice(chars) for _ in range(length - length // 2))
    special = random.choice("!@#$")
    return f"{prefix}{numeric_code}V{version}{suffix}{special}"


# Шаблон 7: Слоговый пароль
def template7(site_name, domain, importance=2, version=0):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    length = max(6, min(importance, 12)) // 2
    result = ""
    for i in range(length):
        if i % 2 == 0:
            result += random.choice(consonants)
        else:
            result += random.choice(vowels)
    site_char = random.choice(site_name.lower().replace(" ", "") + "X").upper()
    domain_char = random.choice(domain.lower().replace(".", "") + "X").upper()
    special = random.choice("!@#$%^&*")
    return f"{site_char}{result}{domain_char}V{version}{special}"


# Шаблон 8: Сегментированный код с поворотом
def template8(site_name, domain, importance=2, version=0):
    chars = string.ascii_letters + string.digits
    length = max(5, min(importance, 10))
    base = ''.join(random.choice(chars) for _ in range(length))
    site_char = random.choice(site_name.lower().replace(" ", "") + "X").upper()
    domain_char = random.choice(domain.lower().replace(".", "") + "X").upper()
    rotated = ''.join(chr(ord(c) + 1) if c.isalnum() else c for c in base)
    special = random.choice("!@#$%^&*")
    return f"{site_char}{base[:length // 2]}{special}{rotated[length // 2:]}V{version}{domain_char}"


# Шаблон 9: Алфавитный шифр
def template9(site_name, domain, importance=2, version=0):
    length = max(4, min(importance, 8))
    chars = string.ascii_lowercase
    base = ''.join(random.choice(chars) for _ in range(length))
    shift = len(site_name) + len(domain) + version % 26
    ciphered = ''.join(chr((ord(c) - 97 + shift) % 26 + 97) for c in base)
    special = random.choice("!@#$%^&*")
    return f"{base.upper()}{special}{ciphered.upper()}V{version}"


# Шаблон 10: Модульный микс
def template10(site_name, domain, importance=2, version=0):
    length = max(6, min(importance, 12))
    result = []
    for i in range(length):
        if i % 3 == 0:
            result.append(random.choice(string.ascii_uppercase))
        elif i % 3 == 1:
            result.append(random.choice(string.digits))
        else:
            result.append(random.choice("!@#$%^&*"))
    site_char = random.choice(site_name.lower().replace(" ", "") + "X").upper()
    domain_char = random.choice(domain.lower().replace(".", "") + "X").upper()
    return f"{site_char}{''.join(result)}V{version}{domain_char}"


# Тестирование всех шаблонов
if __name__ == "__main__":
    test_cases = [
        ("Obsidian-Edward1Mi", "obsidian.md", 16, 0),
        ("SocialNet", "example.com", 10, 1),
        ("", "", 8, 0),
        ("MyApp", "myapp.io", 12, 2),
        ("Banking", "bank.com", 14, 0),
        ("TestSite", "test.org", 6, 3),
        ("", "", 16, 1),
        ("OnlineShop", "shop.ru", 10, 0)
    ]

    templates = [template1, template2, template3, template4, template5, template6, template7, template8, template9,
                 template10]

    for i, template in enumerate(templates, 1):
        print(f"\nШаблон {i}:")
        for site_name, domain, importance, version in test_cases:
            password = template(site_name, domain, importance, version)
            print(f"  site_name='{site_name}', domain='{domain}', importance={importance}, version={version}: {password}")