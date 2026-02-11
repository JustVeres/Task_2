import pytest
from helpers import generate_registration_payload
from api_methods import UserApiMethods

@pytest.fixture # Фикстура для создания и удаления нового юзера
def new_user_register():
    status, body = UserApiMethods.create_user_response()
    token = body["accessToken"]
    yield status, body, token
    UserApiMethods.delete_user_response(token)

@pytest.fixture # Фикстура для создания и удаления существующего юзера
def registered_user():
    payload = generate_registration_payload()
    _, body = UserApiMethods.create_user_with_payload(payload)
    token = body["accessToken"]
    yield payload, token
    UserApiMethods.delete_user_response(token)

#@pytest.fixture # Фикстура для регистрации, авторизация и удаления юзера
#def authorized_user():
#    payload = generate_registration_payload()
#    _, create_body = UserApiMethods.create_user_with_payload(payload)
#    status, login_body = UserApiMethods.login_user_with_payload(payload)
#    token = login_body["accessToken"]
#    yield payload, token, status, login_body
#    UserApiMethods.delete_user_response(token)