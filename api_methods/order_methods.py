import allure
import requests
from urls import Urls


class OrderMethods:

    @staticmethod
    @allure.step('Создать новый заказ')
    def create_order(body):
        return requests.post(Urls.URL_ORDERS_CREATE, json=body)
    
    @staticmethod
    @allure.step('Получить список заказов в теле ответа')
    def get_orders_list():
        return requests.get(Urls.URL_ORDERS_GET_LIST)
