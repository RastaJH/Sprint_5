from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/register"

    # Локаторы
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")

    def set_name(self, name):
        self.type(self.NAME_FIELD, name)

    def set_email(self, email):
        self.type(self.EMAIL_FIELD, email)

    def set_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    def click_register_button(self):
        self.click_element(self.REGISTER_BUTTON)

    def register(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_register_button()

    def click_login_link(self):
        self.click_element(self.LOGIN_LINK)
