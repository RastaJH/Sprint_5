from .base_page import BasePage
from .locators import RegisterLocators

class RegisterPage(BasePage):
    def go(self):
        self.open("register")

    def register(self, name: str, email: str, password: str):
        self.type(RegisterLocators.NAME_INPUT, name)
        self.type(RegisterLocators.EMAIL_INPUT, email)
        self.type(RegisterLocators.PASSWORD_INPUT, password)
        self.click(RegisterLocators.REGISTER_SUBMIT)

    def click_login_link(self):
        self.click(RegisterLocators.LOGIN_LINK)

    def password_error_visible(self) -> bool:
        return self.is_visible(RegisterLocators.PASSWORD_ERROR)
