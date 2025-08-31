from .base_page import BasePage
from .locators import ProfileLocators

class ProfilePage(BasePage):
    def go(self):
        self.open("account/profile")

    def logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)

    def is_opened(self) -> bool:
        return self.is_visible(ProfileLocators.LOGOUT_BUTTON)
