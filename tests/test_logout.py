from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from utils.generators import generate_email, generate_password, generate_name

class TestLogout:

    def test_logout_from_profile(driver):
        """Выход из аккаунта по кнопке 'Выход' в личном кабинете."""
        # Регистрация и вход
        email = generate_email(prefix="logout_user", cohort="013", domain="ya.ru")
        password = generate_password(8)
        reg = RegisterPage(driver)
        reg.go()
        reg.register(generate_name("LogoutUser"), email, password)

        login = LoginPage(driver)
        login.login(email, password)

        profile = ProfilePage(driver)
        profile.go()
        assert profile.is_opened(), "Профиль не открылся перед выходом"

        # Выходим
        profile.logout()

        # Должны попасть на форму входа
        main = MainPage(driver)
        main.go()
        main.click_login_button()
        # Если кнопка 'Войти' видна — считаем, что разлогинились успешно