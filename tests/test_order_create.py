import allure
import pytest
from data import DataOrder
from api_methods.order_methods import OrderMethods


class TestCreateOrder:
    
    @allure.title('Проверка успешного создания заказа')
    @allure.description('Тест на успешное создание заказа с валидными данными, проверка кода ответа и тела ответа')
    @pytest.mark.parametrize('color', 
                             (['BLACK'], ['GREY'], ['BLACK', 'GREY'], [])
                             )
    def test_succes_create_order(self, color):
        body = DataOrder.ORDER_DATA
        body["color"] = color
        
        response = OrderMethods.create_order(body)

        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
        assert 'track' in response.text, f"Response does not contain 'track'. Response: {response.text}"
