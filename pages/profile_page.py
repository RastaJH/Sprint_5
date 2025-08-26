from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProfilePage(BasePage):
    # Локаторы страницы профиля
    PROFILE_LINK = (By.XPATH, ".//a[contains(@class, 'Account_link') and text()='Профиль']")  # Ссылка "Профиль"
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип Stellar Burgers
    
    def click_logout_button(self):
        self.click_element(self.LOGOUT_BUTTON)
    
    def click_constructor_button(self):
        self.click_element(self.CONSTRUCTOR_BUTTON)
    
    def click_logo(self):
        self.click_element(self.LOGO)
    
    def is_logout_button_visible(self):
        try:
            return self.find_element(self.LOGOUT_BUTTON).is_displayed()
        except:
            return False