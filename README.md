# Sprint_7
## Тестирование API учебного сервиса [«Яндекс Самокат»](https://qa-scooter.praktikum-services.ru/). 
<small>Документация: qa-scooter.praktikum-services.ru/docs/.</small>
___

### Структура проекта:
SPRINT_7/
├── `api_methods/`             # Папка для файлов с методами API
│   ├── __init__.py
│   ├── courier_methods.py     # Методы API, связанные с курьерами
│   └── order_methods.py       # Методы API, связанные с заказами
├── `tests/`                   # Папка для файлов с тестами
│   ├── __init__.py
│   ├── test_courier_create.py # Тесты создания курьера
│   ├── test_courier_login.py  # Тесты авторизации курьера
│   ├── test_order_create.py   # Тесты создания заказа
│   └── test_order_list.py     # Тесты получения списка заказов
├── `allure_results/`          # Отчеты Allure с результаты выполнения тестов
├── `.gitignore`               # Правила игнорирования файлов для Git
├── `conftest.py`              # Фикстуры для тестов
├── `data.py`                  # Тестовые данные
├── `helpers.py`               # Вспомогательные функции для тестов
├── `README.md`                # Описание проекта
├── `requirements.txt`         # Зависимости проекта Python
└── `urls.py`                  # URL-эндпоинтов (адреса API)

### Установка:
**1. Клонирование репозитория:** `git clone https://github.com/nlazareff/Sprint_7.git`
**2. Создание виртуального окружения:** `python -m venv venv`
**3. Установка зависимостей:** `pip install -r requirements.txt`

### Покрытие:
В рамках проекта протестированы следующие ручки:
* Создание курьера;
* Логин (авторизацию) курьера;
* Создание заказа;
* Список заказов в теле ответа.


**Тесты запускаются командой** `pytest -v`

**Allure-отчет можно сформировать в формате веб-страницы командой** `allure serve allure_results`
