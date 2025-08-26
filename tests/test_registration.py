import pytest
from utils.data_generator import generate_email, generate_password, generate_name


class TestRegistration:
    @pytest.mark.parametrize("password_length", [6, 10, 15])
    def test_successful_registration(self, register_page, password_length):
        """Успешная регистрация с корректными данными"""
        register_page.go_to_site()
        register_page.click_login_link()
        
        name = generate_name()
        email = generate_email()
        password = generate_password(password_length)
        
        register_page.register(name, email, password)
        
        # После успешной регистрации должна открыться главная страница
        assert "stellarburgers" in register_page.get_current_url()
    
    def test_registration_with_short_password(self, register_page):
        """Ошибка при регистрации с коротким паролем"""
        register_page.go_to_site()
        register_page.click_login_link()
        
        name = generate_name()
        email = generate_email()
        password = generate_password(5)  # Слишком короткий пароль
        
        register_page.register(name, email, password)
        
        # Должно появиться сообщение об ошибке
        error_message = register_page.get_password_error()
        assert error_message is not None
        assert "пароль" in error_message.lower()
    
    def test_registration_with_empty_name(self, register_page):
        """Ошибка при регистрации с пустым именем"""
        register_page.go_to_site()
        register_page.click_login_link()
        
        email = generate_email()
        password = generate_password()
        
        # Не заполняем имя
        register_page.set_email(email)
        register_page.set_password(password)
        register_page.click_register_button()
        
        # Должно появиться сообщение об ошибке
        error_message = register_page.get_error_message()
        assert error_message is not None
    
    def test_registration_with_invalid_email(self, register_page):
        """Ошибка при регистрации с некорректным email"""
        register_page.go_to_site()
        register_page.click_login_link()
        
        name = generate_name()
        password = generate_password()
        
        # Некорректный email
        register_page.register(name, "invalid-email", password)
        
        # Должно появиться сообщение об ошибке
        error_message = register_page.get_error_message()
        assert error_message is not None