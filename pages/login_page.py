from .base_page import BasePage
from .locators import AuthLocators

class LoginPage(BasePage):
    def go(self):
        self.open("login")

    def login(self, email: str, password: str):
        # Используем устойчивые XPATH локаторы
        self.type(AuthLocators.EMAIL_INPUT_X, email)
        self.type(AuthLocators.PASSWORD_INPUT_X, password)
        self.click(AuthLocators.LOGIN_BUTTON)

    def go_to_register(self):
        self.click(AuthLocators.REGISTER_LINK)

    def go_to_forgot(self):
        self.click(AuthLocators.FORGOT_PASSWORD_LINK)
