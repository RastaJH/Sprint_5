import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.profile_page import ProfilePage
from utils.generators import generate_email, generate_password, generate_name

def _ensure_user(driver, email, password):
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

class TestLogin:
    @pytest.mark.parametrize("entry_point, open_method", [
        ("main_button", lambda driver: (MainPage(driver).go(), MainPage(driver).click_login_button())),
        ("account_button", lambda driver: (MainPage(driver).go(), MainPage(driver).go_to_account())),
        ("register_form", lambda driver: (RegisterPage(driver).go(), RegisterPage(driver).click_login_link())),
        ("forgot_form", lambda driver: (LoginPage(driver).go(), LoginPage(driver).go_to_forgot(), LoginPage(driver).go())),
    ])
    def test_login_via_different_entry_points(self, driver, existing_user, entry_point, open_method):
        email, password = existing_user
        open_method(driver)
        login = LoginPage(driver)
        login.login(email, password)
        profile = ProfilePage(driver)
        profile.go()
        assert profile.is_opened(), f"Не удалось войти способом: {entry_point}"
