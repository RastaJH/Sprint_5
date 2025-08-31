from .base_page import BasePage
from .locators import MainPageLocators, CommonLocators

class MainPage(BasePage):
    def go(self):
        self.open("")

    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_MAIN_BUTTON)

    def go_to_account(self):
        self.click(MainPageLocators.ACCOUNT_BUTTON)

    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    def click_logo(self):
        self.click(MainPageLocators.LOGO_LINK)

    # Tabs
    def open_tab_buns(self):
        self.click(MainPageLocators.TAB_BUNS)

    def open_tab_sauces(self):
        self.click(MainPageLocators.TAB_SAUCES)

    def open_tab_toppings(self):
        self.click(MainPageLocators.TAB_TOPPINGS)

    def active_tab_text(self) -> str:
        return self.text_of(MainPageLocators.ACTIVE_TAB)

    def constructor_header_visible(self) -> bool:
        return self.is_visible(CommonLocators.HEADER_CONSTRUCTOR)
