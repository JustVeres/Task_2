import pytest
import requests
from helpers import generate_payload
from api_methods import UserApiMethods
from data.data_urls import Urls
from data.data_requests import Payloads

@pytest.fixture # Фикстура для создания и удаления нового юзера
def new_user_register():
    status, body = UserApiMethods.create_user_response()
    token = body["accessToken"]
    yield status, body, token
    UserApiMethods.delete_user_response(token)

@pytest.fixture # Фикстура для создания и удаления существующего юзера
def registered_user():
    payload = generate_payload()
    _, body = UserApiMethods.create_user_with_payload(payload)
    token = body["accessToken"]
    yield payload, token
    UserApiMethods.delete_user_response(token)

@pytest.fixture
def authorized_user():
    payload = generate_payload()
    _, body = UserApiMethods.create_user_with_payload(payload)
    token = body["accessToken"]
    yield payload, token
    UserApiMethods.delete_user_response(token)

@pytest.fixture
def valid_ingredients():
    response = requests.get(Urls.INGREDIENTS_URL)
    ingredients = response.json()["data"]
    return [ingredients[0]["_id"], ingredients[1]["_id"]]

@pytest.fixture
def payload_order():
    payload = Payloads.create_order_payload()
    return payload

@pytest.fixture
def random_payload():
    payload = generate_payload()
    return payload

@pytest.fixture
def create_user_payload():
    payload = Payloads.request_create_user_payload()
    return payload
