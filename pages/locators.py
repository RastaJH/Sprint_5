from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.nomoreparties.site/"

class MainPageLocators:
    LOGIN_MAIN_BUTTON = (By.XPATH, "//button[.='Войти в аккаунт']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[.='Конструктор']")
    LOGO_LINK = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]//a")
    ACCOUNT_BUTTON = (By.XPATH, "//p[.='Личный Кабинет' or .='Личный кабинет']")

    # Tabs
    TAB_BUNS = (By.XPATH, "//span[contains(@class,'tab_tab__1SPyG') and text()='Булки']")
    TAB_SAUCES = (By.XPATH, "//span[contains(@class,'tab_tab__1SPyG') and text()='Соусы']")
    TAB_TOPPINGS = (By.XPATH, "//span[contains(@class,'tab_tab__1SPyG') and text()='Начинки']")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span")

class AuthLocators:
    EMAIL_INPUT = (By.NAME, "name")  # на странице логина поле email имеет name='name'
    PASSWORD_INPUT = (By.NAME, "Пароль")  # иногда локаторы отличаются; продублируем универсальный XPATH ниже
    EMAIL_INPUT_X = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT_X = (By.XPATH, "//input[@name='Пароль' or @type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[.='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[.='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[.='Восстановить пароль']")

class RegisterLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_SUBMIT = (By.XPATH, "//button[.='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[.='Войти']")
    PASSWORD_ERROR = (By.XPATH, "//*[contains(text(),'Минимальный пароль') or contains(text(),'Некорректный пароль') or contains(text(),'Минимальный')]")

class ProfileLocators:
    PROFILE_HEADER = (By.XPATH, "//a[contains(@class,'Account_link_active')] | //h2[contains(text(),'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[.='Выход']")

# Общие
class CommonLocators:
    HEADER_CONSTRUCTOR = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
