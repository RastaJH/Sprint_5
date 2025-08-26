# Sprint 5 – Автотесты для Stellar Burgers

Проект содержит автотесты на Selenium для проверки функционала сервиса Stellar Burgers.

## Структура проекта
- `tests/` – тесты, сгруппированные по функциональности
- `pages/` – Page Object классы
- `helpers/` – генераторы данных
- `conftest.py` – фикстуры Pytest

## Запуск тестов
Убедитесь, что установлен Python 3.10+, pytest и Selenium.

```bash
pip install -r requirements.txt
pytest -v
```

По умолчанию используется ChromeDriver. Для запуска в headless-режиме добавьте флаг:
```bash
pytest -v --headless
```
