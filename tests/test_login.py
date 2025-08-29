import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.profile_page import ProfilePage
from utils.generators import generate_email, generate_password, generate_name

def _ensure_user(driver, email, password):
    """Помощник: создать пользователя через форму регистрации (если требуется)."""
    reg = RegisterPage(driver)
    reg.go()
    name = generate_name("User")
    reg.register(name, email, password)

@pytest.fixture
def existing_user(driver):
    email = generate_email(prefix="login_user", cohort="013", domain="ya.ru")
    password = generate_password(8)
    _ensure_user(driver, email, password)
    return email, password

@pytest.mark.parametrize("entry_point", ["main_button", "account_button", "register_form", "forgot_form"])
def test_login_via_different_entry_points(driver, existing_user, entry_point):
    """Вход разными способами: с главной, из ЛК, из формы регистрации, из формы восстановления пароля."""
    email, password = existing_user
    main = MainPage(driver)

    if entry_point == "main_button":
        main.go()
        main.click_login_button()
    elif entry_point == "account_button":
        main.go()
        main.go_to_account()
    elif entry_point == "register_form":
        # Открыть регистрацию и нажать 'Войти'
        reg = RegisterPage(driver)
        reg.go()
        reg.click_login_link()
    elif entry_point == "forgot_form":
        login = LoginPage(driver)
        login.go()
        login.go_to_forgot()
        # На странице восстановления обычно есть ссылка 'Войти'
        login.go()  # возвращаемся на страницу логина

    login = LoginPage(driver)
    login.login(email, password)

    profile = ProfilePage(driver)
    profile.go()
    assert profile.is_opened(), f"Не удалось войти способом: {entry_point}"
