import allure
import pytest
from helpers import generate_registration_payload
from api_methods import UserApiMethods
from data.data_response import ErrorResponse as ER
from data.data_requests import Payloads

class TestCreateUserApi:

    @allure.title("Успешное создание пользователя")
    def test_create_user(self, new_user_register):
        with allure.step("Создать нового пользователя"):
            status, body, token = new_user_register

        with allure.step("Проверить успешный статус ответа"):
            assert status == 200

        with allure.step("Проверить структуру и данные пользователя"):
            assert body["success"] is True
            assert "accessToken" in body
            assert body["user"]["email"]
            assert body["user"]["name"]


    @allure.title("Нельзя создать уже зарегистрированного пользователя")
    def test_create_existing_user(self, registered_user):
        payload, _ = registered_user

        with allure.step("Отправить запрос на повторную регистрацию"):
            status, body = UserApiMethods.create_user_with_payload(payload)

        with allure.step("Проверить статус ошибки"):
            assert status == 403

        with allure.step("Проверить сообщение об ошибке"):
            assert body["message"] == ER.USER_ALREADY_EXISTS_RESPONSE


    @allure.title("Нельзя создать пользователя без обязательных полей")
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_create_user_without_required_field(self, field):
        payload = generate_registration_payload()

        with allure.step(f"Очистить обязательное поле: {field}"):
            payload[field] = ""

        with allure.step("Отправить запрос на создание пользователя"):
            status, body = UserApiMethods.create_user_with_payload(payload)

        with allure.step("Проверить статус ошибки"):
            assert status == 403

        with allure.step("Проверить текст ошибки"):
            assert body["success"] is False
            assert body["message"] == ER.REQUIRED_FIELDS_USER_RESPONSE


    @allure.title("Нельзя создать пользователя с пустыми полями")
    def test_create_user_with_empty_body(self):
        payload = Payloads.request_create_user_payload()
        with allure.step("Отправить запрос на создание пользователя"):
            status, body = UserApiMethods.create_user_with_payload(payload)

        with allure.step("Проверить ошибку валидации"):
            assert status == 403
            assert body["message"] == ER.REQUIRED_FIELDS_USER_RESPONSE


    @allure.title("Нельзя создать пользователя без обязательного ключа")
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_create_user_without_field_key(self, field):
        payload = generate_registration_payload()

        with allure.step(f"Удалить обязательный ключ: {field}"):
            payload.pop(field)
        with allure.step("Отправить запрос на создание пользователя"):
            status, body = UserApiMethods.create_user_with_payload(payload)
        with allure.step("Проверить статус и сообщение ошибки"):
            assert status == 403
            assert body["message"] == ER.REQUIRED_FIELDS_USER_RESPONSE
