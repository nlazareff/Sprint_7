import allure
import requests
from urls import Urls


class CourierMethods:

    @staticmethod
    @allure.step('Создать курьера')
    def create_courier(body):
        return requests.post(url=Urls.URL_COURIER_CREATE, json=body)

    @staticmethod
    @allure.step('Авторизовать существующего курьера')
    def login_courier(body):
        return requests.post(url=Urls.URL_COURIER_LOGIN, json=body)

    @staticmethod
    @allure.step('Удалить курьера по id')
    def delete_courier(courier_id):
        return requests.delete(f'{Urls.URL_COURIER_DELETE}/{courier_id}')
