from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    url = "https://stellarburgers.nomoreparties.site/login"

    # Локаторы
    EMAIL_FIELD = (By.XPATH, "//input[@name='name' or @type='text']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(text(),'Личный Кабинет')]")

    def login(self, email, password):
        self.type(self.EMAIL_FIELD, email)
        self.type(self.PASSWORD_FIELD, password)
        self.click_element(self.SUBMIT_BUTTON)

    def click_register_link(self):
        self.click_element(self.REGISTER_LINK)

    def click_recover_password_link(self):
        self.click_element(self.RECOVER_PASSWORD_LINK)

    def click_login_link(self):
        self.click_element(self.LOGIN_LINK)

    def click_personal_account_button(self):
        self.click_element(self.PERSONAL_ACCOUNT_BUTTON)
