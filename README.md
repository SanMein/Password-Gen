# Password Generator
### Описание (Русский)
***Password Generator*** — это простой Python-скрипт для генерации уникальных паролей на основе заданного шаблона. Проект разработан для создания безопасных и структурированных паролей, которые подходят для различных сайтов и сервисов. Шаблон пароля включает пять компонентов: код сайта (сервиса), случайный код, индекс домена, версию пароля и специальный символ. Генерация учитывает название сайта (или сервиса), домен, уровень важности и версию пароля, обеспечивая вариативность и уникальность.


### Основные возможности
- Гибкий шаблон пароля: Пароль формируется в формате `<site_code>-<random_code>-<domain_index>-<version>-<special_char>`.
- Код сайта (`site_code`): Генерируется из названия сайта (4 символа), с рандомизацией порядка символов для вариативности (например, для "wararsmirrr" возможны "WAMR", "AAMR"). Если название пустое, используется случайная комбинация заглавных букв и цифр.
- Случайный код (`random_code`): Алфавитно-цифровой код длиной от 5 до 16 символов, зависящий от уровня важности (по умолчанию 10).
- Индекс домена (`domain_index`): Генерируется из названия домена (3-4 символа) с рандомизацией. Например, для "com" возможны "OCM", "MOC". Если домен пустой, используется случайная комбинация.
- Версия пароля (`version`): Позволяет отслеживать обновления пароля (например, V0, V1). Поддерживается версия 0.
- Специальный символ (`special_char`): Случайный символ из набора `!@#$%^&*` для соответствия требованиям безопасности.


### Установка
1. Убедитесь, что у вас установлен Python 3.6 или выше.
2. Скрипт использует только стандартные библиотеки Python (`hashlib`, `random`, `string`), поэтому дополнительные зависимости не требуются.
3. Скачайте файл Password-Gen.py из репозитория.


### Использование
1. Поместите Password-Gen.py в вашу рабочую директорию.
2. Запустите скрипт через Python:
`python Password-Gen.py`
3. Используйте функцию `generate_password(site_name, domain, importance, version)` для генерации пароля:
`site_name`: Название сайта (например, "wararsmirrr").
`domain`: Домен сайта (например, "com", "gmail").
`importance`: Уровень важности (5-16, определяет длину `random_code`).
`version`: Версия пароля (0 или больше).
4. Пример вызова в Python:
`from Password-Gen import generate_password
print(generate_password("wararsmirrr", "com", importance=5, version=0))`


### Структура кода
- `generate_site_code(site_name)`: Создает 4-символьный код на основе названия сайта с рандомизацией.
- `generate_random_code(importance)`: Генерирует алфавитно-цифровой код длиной от 5 до 16 символов.
- `generate_domain_index(domain)`: Создает 3-4-символьный индекс домена с рандомизацией.
- `generate_special_char()`: Выбирает случайный специальный символ.
- `generate_password(site_name, domain, importance, version)`: Объединяет компоненты в итоговый пароль.


### Примеры вывода
Вход: `site_name="wararsmirrr", domain="com", importance=5, version=0`
`WAMR-aB9k2-OCM-V0-!`
Вход: `site_name="wararsmirrr", domain="com", importance=5, version=0` (повторный запуск)
`AAMR-p7q3w-MOC-V0-@`
Вход: `site_name="", domain="", importance=5, version=0`
`K7P4-x9m2n-X9Q-V0-#`


# Description (English)
Password Generator is a simple Python script designed to generate unique passwords based on a structured template. The project aims to create secure and consistent passwords suitable for various websites and services. The password template consists of five components: site code (or service), random code, domain index, password version, and special character. The generation process takes into account the site name, domain, importance level, and password version, ensuring variability and uniqueness.


### Key Features
- Flexible Password Template: Passwords are generated in the format `<site_code>-<random_code>-<domain_index>-<version>-<special_char>`.
- Site Code (`site_code`): Generated from the site name (4 characters) with randomized character order for variability (e.g., "WAMR", "AAMR" for "wararsmirrr"). If the site name is empty, a random combination of uppercase letters and digits is used.
- Random Code (`random_code`): An alphanumeric code ranging from 5 to 16 characters, depending on the importance level (default is 10).
- Domain Index (`domain_index`): Generated from the domain name (3-4 characters) with randomization. For example, "OCM", "MOC" for "com". If the domain is empty, a random combination is used.
- Password Version (`version)`: Tracks password updates (e.g., V0, V1). Supports version 0.
- Special Character (`special_char`): A random character from the set `!@#$%^&*` to meet security requirements.


### Installation
1. Ensure you have Python 3.6 or higher installed.
2. The script uses only standard Python libraries (`hashlib`, `random`, `string`), so no additional dependencies are required.
3. Download the Password-Gen.py file from the repository.


### Usage
1. Place Password-Gen.py in your working directory.
2. Run the script using Python:
`python Password-Gen.py`
3. Use the `generate_password(site_name, domain, importance, version)` function to generate a password:
`site_name`: The name of the site (e.g., "wararsmirrr").
`domain`: The site’s domain (e.g., "com", "gmail").
`importance`: Importance level (5-16, determines the length of random_code).
`version`: Password version (0 or higher).
4. Example usage in Python:
`from Password-Gen import generate_password
print(generate_password("wararsmirrr", "com", importance=5, version=0))`


### Code Structure
- `generate_site_code(site_name)`: Creates a 4-character code based on the site name with randomization.
- `generate_random_code(importance)`: Generates an alphanumeric code of 5 to 16 characters.
- `generate_domain_index(domain)`: Creates a 3-4-character domain index with randomization.
- `generate_special_char()`: Selects a random special character.
- `generate_password(site_name, domain, importance, version)`: Combines components into the final password.


### Example Output
Input: `site_name="wararsmirrr", domain="com", importance=5, version=0`
`WAMR-aB9k2-OCM-V0-!`:

Input: `site_name="wararsmirrr", domain="com", importance=5, version=0` (repeated run)
`AAMR-p7q3w-MOC-V0-@`:

Input: `site_name="", domain="", importance=5, version=0`
`K7P4-x9m2n-X9Q-V0-#`
