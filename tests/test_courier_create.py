import allure
import pytest
from data import DataCourier
from api_methods.courier_methods import CourierMethods
from helpers import generate_random_courier_body


class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера')
    @allure.description('Тест на успешное создание нового курьера с валидными данными, проверка кода ответа и тела ответа')
    def test_succes_create_courier(self):
        body = generate_random_courier_body()
        response = CourierMethods.create_courier(body)

        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
        assert response.json() == {'ok': True}, f"Expected {{'ok': True}}, but got {response.json()}"

    @allure.title('Проверка ошибки при создании двух одинаковых курьеров')
    @allure.description('Тест проверяет, что при создании двух курьеров с одинаковыми данными система выдает ошибку 409 Conflict')
    def test_error_create_two_identical_couriers(self, courier):
        body, *_ = courier
        response_second = CourierMethods.create_courier(body)

        assert response_second.status_code == 409, f"Expected status code 409, but got {response_second.status_code}"

    @allure.title('Проверка ошибки при создании курьера с существующим логином')
    @allure.description('Тест проверяет, что при создании курьера с существующим логином и другим паролем, система выдает ошибку 409 "Этот логин уже используется"')
    def test_error_create_couriers_with_existing_login(self, courier):
        body, *_ = courier

        with allure.step('Поменять пароль в body'):
            body["password"] = "urfehcnsjdijf6438"
            
        response_second = CourierMethods.create_courier(body)
        
        assert response_second.status_code == 409, f"Expected status code 409, but got {response_second.status_code}"
        assert response_second.json()['message'] == 'Этот логин уже используется', f"Expected 'Этот логин уже используется', but got '{response_second.json()['message']}'"

    @allure.title('Проверка ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description('Тест на невозможность зарегистрировать курьера без заполнения обязательных полей Login и Password, проверяет код ответа и тело ответа')
    @pytest.mark.parametrize('body', 
                         [{'login': '', 'password': DataCourier.UNREGISTERED_COURIER_DATA['password']},
                          {'login': DataCourier.UNREGISTERED_COURIER_DATA['login'], 'password': ''}]
                          )
    def test_error_create_courier_with_empty_required_fields(self, body):
        response = CourierMethods.create_courier(body)

        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи', f"Expected 'Недостаточно данных для создания учетной записи', but got '{response.json()['message']}'"
