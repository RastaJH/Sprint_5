import pytest
from pages.main_page import MainPage

class TestConstructorTabs:

    @pytest.mark.parametrize("open_method, expected", [
        ("open_tab_buns", "Булки"),
        ("open_tab_sauces", "Соусы"),
        ("open_tab_toppings", "Начинки"),
    ])
    def test_constructor_tabs_switch(driver, open_method, expected):
        """Раздел 'Конструктор': переходы по вкладкам 'Булки', 'Соусы', 'Начинки' (параметризация)."""
        main = MainPage(driver)
        main.go()
        getattr(main, open_method)()
        assert main.active_tab_text() == expected, f"Активная вкладка должна быть: {expected}"

    def test_go_from_account_to_constructor_and_logo(driver):
        """Переход из личного кабинета в конструктор по кнопке 'Конструктор' и по клику на логотип."""
        main = MainPage(driver)
        main.go()
        # Проверяем переход по кнопке 'Конструктор'
        main.go_to_constructor()
        assert main.constructor_header_visible(), "Не открылся конструктор по кнопке 'Конструктор'"
        # Проверяем переход по лого
        main.click_logo()
        assert main.constructor_header_visible(), "Не открылся конструктор по клику на логотип"