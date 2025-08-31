from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.generators import generate_email, generate_password, generate_name

class TestAccountNavigation:

    def test_go_to_account_from_header(driver):
        """Переход в личный кабинет по клику на 'Личный кабинет'."""
        # Подготовим пользователя и войдём
        email = generate_email(prefix="nav_user", cohort="013", domain="ya.ru")
        password = generate_password(8)
        reg = RegisterPage(driver)
        reg.go()
        reg.register(generate_name("NavUser"), email, password)

        login = LoginPage(driver)
        login.login(email, password)

        main = MainPage(driver)
        main.go_to_account()

        profile = ProfilePage(driver)
        assert profile.is_opened(), "Личный кабинет не открылся по клику в хедере"