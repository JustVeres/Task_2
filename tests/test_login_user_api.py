import allure
import pytest
from api_methods import UserApiMethods
from data.data_response import ErrorResponse as ER

"""Создание пользователя"""

@allure.title("Логин под существующим пользователем")
def test_login_existing_user(registered_user):
    payload, _ = registered_user

    with allure.step("Выполнить авторизацию под зарегистрированным пользователем"):
        status, body = UserApiMethods.login_user_with_payload(payload)

    with allure.step("Проверить успешный ответ"):
        assert status == 200
        assert body["success"] is True
        assert "accessToken" in body
        assert "refreshToken" in body
        assert body["user"]["email"] == payload["email"]
        assert body["user"]["name"] == payload["name"]


@allure.title("Логин с неверным email или password")
@pytest.mark.parametrize("field", ["email", "password"])
def test_login_with_wrong_credentials(field, random_payload):
    with allure.step("Создать нового пользователя"):
        UserApiMethods.create_user_with_payload(random_payload)

    with allure.step(f"Сломать поле {field}"):
        wrong_payload = random_payload.copy()
        wrong_payload[field] = "wrong_value"

    with allure.step("Попытаться авторизоваться с некорректными данными"):
        status, body = UserApiMethods.login_user_with_payload(wrong_payload)

    with allure.step("Проверить ошибку авторизации"):
        assert status == 401
        assert body["success"] is False
        assert body["message"] == ER.INCORRECT_FIELDS_RESPONSE
