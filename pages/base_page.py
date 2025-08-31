from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BASE_URL

DEFAULT_TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, path: str = ""):
        url = BASE_URL.rstrip("/") + "/" + path.lstrip("/")
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text: str, clear: bool = True):
        el = self.wait.until(EC.presence_of_element_located(locator))
        if clear:
            el.clear()
        el.send_keys(text)

    def text_of(self, locator) -> str:
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

    def is_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def current_url(self) -> str:
        return self.driver.current_url
