import pytest
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.generators import generate_email, generate_password, generate_name

@pytest.mark.parametrize("pwd_len", [6, 8, 12])
def test_success_register_with_valid_passwords(driver, pwd_len):
    """Успешная регистрация с валидными длинами пароля (параметризация)."""
    main = MainPage(driver)
    main.go()
    main.click_login_button()

    login = LoginPage(driver)
    login.go_to_register()

    reg = RegisterPage(driver)
    name = generate_name("Autotest User")
    email = generate_email(prefix="autotest_user", cohort="013", domain="ya.ru")
    password = generate_password(pwd_len)
    reg.register(name, email, password)

    # После регистрации ожидаем попасть на страницу логина/аккаунта и суметь войти
    # В некоторых версиях нужно повторно нажать "Войти", поэтому проверим вход:
    login.login(email, password)
    profile = ProfilePage(driver)
    profile.go()  # переходим в профиль
    assert profile.is_opened(), "Профиль не открылся после регистрации и входа"

@pytest.mark.parametrize("pwd_len", [1, 3, 5])
def test_register_with_short_password_shows_error(driver, pwd_len):
    """Ошибка при регистрации с коротким паролем (<6)."""
    reg = RegisterPage(driver)
    reg.go()
    name = generate_name("ShortPwd")
    email = generate_email(prefix="short_pwd", cohort="013", domain="ya.ru")
    password = "a"*pwd_len
    reg.register(name, email, password)
    assert reg.password_error_visible(), "Не отображается ошибка для короткого пароля"
