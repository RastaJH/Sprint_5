import random
import string
import uuid

def generate_email(prefix: str = "test", cohort: str = "013", domain: str = "yandex.ru") -> str:
    """Генерирует email в формате имя_фамилия_номер_когорты_3цифры@домен.
    Для простоты используем prefix как 'имя_фамилия', добавляем номер когорты и 3 цифры.
    """
    tail = f"{random.randint(100, 999)}"
    name_surname = prefix.replace(" ", "_").lower()
    return f"{name_surname}_{cohort}_{tail}@{domain}"

def generate_password(length: int = 8) -> str:
    """Генерирует пароль указанной длины (буквы+цифры). Минимум 6 символов по заданию."""
    length = max(length, 6)
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))

def generate_name(prefix: str = "Test User") -> str:
    """Простое имя: TestUser-xxxx"""
    return prefix.replace(" ", "") + "-" + str(uuid.uuid4())[:8]
