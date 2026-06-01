import pytest
from api_methods.courier_methods import CourierMethods
from helpers import generate_random_courier_body


@pytest.fixture(scope="function")
def courier():
    body = generate_random_courier_body()
    response = CourierMethods.create_courier(body)

    courier_id = None
    if response.status_code == 201:
        courier_id = CourierMethods.login_courier(body=body).json()['id']

    yield body, response, courier_id

    if courier_id is not None:
        CourierMethods.delete_courier(courier_id)
