from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.nomoreparties.site"

# --- Главная страница ---
MAIN_CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор" в шапке
MAIN_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")  # Логотип Stellar Burgers
MAIN_LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
MAIN_PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет" в шапке

# --- Вкладки конструктора ---
TAB_BUNS = (By.XPATH, "//span[text()='Булки']")
TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']")
TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']")
TAB_ACTIVE = (By.XPATH, "//div[contains(@class,'tab_tab__') and .//span[contains(@class,'current')]]/span")  # Активная вкладка

# --- Страница логина ---
LOGIN_EMAIL = (By.NAME, "name")  # Поле Email (на сайте поле имеет name='name')
LOGIN_PASSWORD = (By.NAME, "Пароль")  # Поле Пароль
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка Войти
LOGIN_REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Ссылка "Зарегистрироваться"
LOGIN_FORGOT_LINK = (By.LINK_TEXT, "Восстановить пароль")  # Ссылка "Восстановить пароль"

# --- Восстановление пароля ---
FORGOT_TO_LOGIN_LINK = (By.LINK_TEXT, "Войти")  # Ссылка "Войти" на странице восстановления пароля

# --- Страница регистрации ---
REG_NAME = (By.NAME, "name")  # Поле Имя
REG_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email
REG_PASSWORD = (By.NAME, "Пароль")  # Поле Пароль
REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка Зарегистрироваться
REG_TO_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Ссылка "Войти" из регистрации
REG_ERROR = (By.XPATH, "//p[contains(@class,'input__error') and text()]")  # Текст ошибки под полем

# --- Профиль ---
PROFILE_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка Выход

# --- Общие ---
H1_TITLE = (By.TAG_NAME, "h2")  # Заголовок секции конструктора (на главной)
