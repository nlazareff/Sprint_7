import allure
from api_methods.order_methods import OrderMethods


class TestOrderList:
    
    @allure.title('Проверка списка заказов в body')
    @allure.description('Тест на возврат списка заказов в теле ответа, проверяет тело ответа')
    def test_succes_get_orders_list(self):
        response = OrderMethods.get_orders_list()

        assert type(response.json()['orders']) == list, f"Expected type list, but got {type(response.json()['orders'])}"
        assert "orders" in response.text, f"Response does not contain 'orders'. Response: {response.text}"
