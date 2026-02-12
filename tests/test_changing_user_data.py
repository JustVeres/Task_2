import allure
from api_methods import UserApiMethods
from data.data_response import ErrorResponse as ER

"""Изменение данных пользователя"""

@allure.title("Изменение данных пользователя с авторизацией")
def test_change_user_data_with_auth(authorized_user):
    _, token = authorized_user

    with allure.step("Отправить запрос на изменение данных пользователя с токеном"):
        status, body, new_payload = UserApiMethods.changing_user_data_payload(token)

    with allure.step("Проверить успешный статус ответа"):
        assert status == 200

    with allure.step("Проверить, что данные пользователя обновились"):
        assert body["success"] is True
        assert body["user"]["email"] == new_payload["email"]
        assert body["user"]["name"] == new_payload["name"]


@allure.title("Изменение данных пользователя без авторизации")
def test_change_user_data_without_auth():
    with allure.step("Отправить запрос на изменение данных без токена"):
        status, body, _ = UserApiMethods.changing_user_data_payload(access_token="")

    with allure.step("Проверить статус ошибки авторизации"):
        assert status == 401

    with allure.step("Проверить сообщение об ошибке"):
        assert body["success"] is False
        assert body["message"] == ER.SHOULD_BE_AUTHORISED_RESPONSE
