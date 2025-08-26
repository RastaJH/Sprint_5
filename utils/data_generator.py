import random
import string


def generate_email(cohort_number="99", additional_digits=3):
    """Генерация email в формате имя_фамилия_номер_когорты_любые_3_цифры@домен"""
    first_name = "test"
    last_name = "user"
    random_digits = ''.join(random.choices(string.digits, k=additional_digits))
    
    email = f"{first_name}_{last_name}_{cohort_number}_{random_digits}@yandex.ru"
    return email


def generate_password(length=6):
    """Генерация пароля минимальной длины"""
    if length < 6:
        length = 6
    
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password


def generate_name():
    """Генерация имени"""
    names = ["Иван", "Мария", "Петр", "Анна", "Сергей", "Ольга", "Алексей", "Елена"]
    return random.choice(names)