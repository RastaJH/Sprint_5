from pages.main_page import MainPage

# Переход в личный кабинет
def test_go_to_profile_from_header(driver):
    main = MainPage(driver)
    main.open_main()
    main.go_to_profile()
    assert driver.current_url.endswith("/login")  # попадаем на логин, если не авторизованы

# Переход в конструктор по кнопке "Конструктор"
def test_go_to_constructor_from_header(driver):
    main = MainPage(driver)
    main.open_main()
    main.go_to_constructor()
    assert "stellarburgers" in driver.current_url

# Переход в конструктор по клику на логотип
def test_go_to_constructor_by_logo(driver):
    main = MainPage(driver)
    main.open_main()
    main.click_logo()
    assert "stellarburgers" in driver.current_url

# Раздел «Конструктор»: вкладки
def test_constructor_tabs(driver):
    main = MainPage(driver)
    main.open_main()

    main.open_tab_fillings()
    assert main.active_tab_text() in ("Начинки", "Соусы", "Булки")

    main.open_tab_sauces()
    assert main.active_tab_text() in ("Соусы", "Начинки", "Булки")

    main.open_tab_buns()
    assert main.active_tab_text() in ("Булки", "Соусы", "Начинки")
