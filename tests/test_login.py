import pytest
from utils.data_generator import generate_email, generate_password, generate_name


class TestLogin:
    def test_login_from_main_page_button(self, main_page, login_page):
        """Вход по кнопке «Войти в аккаунт» на главной"""
        main_page.go_to_site()
        main_page.click_login_button()
        
        # Должна открыться страница логина
        assert "login" in login_page.get_current_url().lower()
    
    def test_login_from_personal_account_button(self, main_page, login_page):
        """Вход через кнопку «Личный кабинет»"""
        main_page.go_to_site()
        main_page.click_personal_account_button()
        
        # Должна открыться страница логина
        assert "login" in login_page.get_current_url().lower()
    
    def test_login_from_register_page(self, register_page, login_page):
        """Вход через кнопку в форме регистрации"""
        register_page.go_to_site()
        register_page.click_login_link()
        register_page.click_login_link()  # Переход на страницу регистрации и обратно
        
        # Должна открыться страница логина
        assert "login" in login_page.get_current_url().lower()
    
    def test_login_from_recovery_page(self, login_page):
        """Вход через кнопку в форме восстановления пароля"""
        login_page.go_to_site()
        login_page.click_recover_password_link()
        login_page.click_login_link()
        
        # Должна открыться страница логина
        assert "login" in login_page.get_current_url().lower()