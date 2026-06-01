import allure
import pytest
from data import DataCourier
from api_methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Тест на успешную авторизацию курьера с валидными данными, проверка кода ответа и тела ответа')
    def test_succes_login_courier(self, courier):
        body, *_ = courier
        response_second = CourierMethods.login_courier(body)

        assert response_second.status_code == 200, f'Expected status code 200, but got {response_second.status_code}'
        assert 'id' in response_second.text, f"Response does not contain 'id'. Response: {response_second.text}"

    @allure.title('Проверка ошибки при авторизации курьера с незаполненными обязательными полями')
    @allure.description('Тест на невозможность авторизовать курьера без заполнения обязательных полей Login и Password. Проверяет код ответа и тело ответа')
    @pytest.mark.parametrize('body', 
                             [{'login': '', 'password': DataCourier.COURIER_DATA['password']},
                              {'login': DataCourier.COURIER_DATA['login'], 'password': ''}]
                              )
    def test_error_login_courier_with_empty_required_fields(self, body):
        response = CourierMethods.login_courier(body)

        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        assert response.json()['message'] == 'Недостаточно данных для входа', f"Expected 'Недостаточно данных для входа', but got '{response.json()['message']}'"

    @allure.title('Проверка ошибки авторизации курьера с неправильным логином или паролем')
    @allure.description('Тест на невозможность авторизовать курьера, если неправильно указать логин или пароль. Проверяет код ответа и тело ответа')
    @pytest.mark.parametrize('body', 
                             [{'login': DataCourier.COURIER_DATA['login'], 'password': DataCourier.UNREGISTERED_COURIER_DATA['password']},
                              {'login': DataCourier.UNREGISTERED_COURIER_DATA['login'], 'password': DataCourier.COURIER_DATA['password']}]
                              )
    def test_error_login_courier_with_incorrect_login_or_password(self, body):
        response = CourierMethods.login_courier(body)

        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
        assert response.json()['message'] == 'Учетная запись не найдена', f"Expected 'Учетная запись не найдена', but got '{response.json()['message']}'"

    @allure.title('Проверка ошибки авторизации курьера под несуществующим пользователем')
    @allure.description('Тест на невозможность авторизовать курьера, если указать несуществующие логин и пароль. Проверяет код ответа и тело ответа')
    def test_error_login_courier_with_incorrect_login_and_password(self):
        body = DataCourier.UNREGISTERED_COURIER_DATA
        response = CourierMethods.login_courier(body)

        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
        assert response.json()['message'] == 'Учетная запись не найдена', f"Expected 'Учетная запись не найдена', but got '{response.json()['message']}'"
