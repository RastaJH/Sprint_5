from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site/"

    # Локаторы
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    PROFILE_BUTTON = (By.XPATH, "//*[contains(text(),'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[contains(text(),'Конструктор')]")
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]//a")
    BUNS_TAB = (By.XPATH, "//span[contains(text(),'Булки')]")
    SAUCES_TAB = (By.XPATH, "//span[contains(text(),'Соусы')]")
    FILLINGS_TAB = (By.XPATH, "//span[contains(text(),'Начинки')]")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span" )

    def open_main(self):
        self.driver.get(self.URL)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def go_to_profile(self):
        self.click_element(self.PROFILE_BUTTON)

    def go_to_constructor(self):
        self.click_element(self.CONSTRUCTOR_BUTTON)

    def click_logo(self):
        self.click_element(self.LOGO)

    def open_tab_buns(self):
        self.click_element(self.BUNS_TAB)

    def open_tab_sauces(self):
        self.click_element(self.SAUCES_TAB)

    def open_tab_fillings(self):
        self.click_element(self.FILLINGS_TAB)

    def active_tab_text(self):
        return self.get_text(self.ACTIVE_TAB)

    def click_personal_account_button(self):
        self.click_element(self.PROFILE_BUTTON)
