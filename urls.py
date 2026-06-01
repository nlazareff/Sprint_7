class Urls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    URL_COURIER_CREATE = f'{MAIN_URL}/api/v1/courier'
    URL_COURIER_LOGIN = f'{MAIN_URL}/api/v1/courier/login'
    URL_COURIER_DELETE = f'{MAIN_URL}/api/v1/courier/{{courier_id}}'
    URL_ORDERS_CREATE = f'{MAIN_URL}/api/v1/orders'
    URL_ORDERS_GET_LIST = f'{MAIN_URL}/api/v1/orders'
