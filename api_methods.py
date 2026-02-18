import requests
import allure
from helpers import generate_payload, random_string
from data.data_requests import Payloads
from data.data_urls import Urls

class UserApiMethods:

    @staticmethod
    @allure.step("Создать/зарегистрировать пользователя")
    def create_user_response():
        response = requests.post(Urls.AUTH_REGISTER_URL, json=generate_payload())
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Удалить пользователя")
    def delete_user_response(access_token: str):
        headers = {"Authorization": access_token}
        response = requests.delete(Urls.AUTH_USER_URL, headers=headers)
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Создать существующего пользователя")
    def create_user_with_payload(payload: dict):
        response = requests.post(Urls.AUTH_REGISTER_URL, json=payload)
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Выполнить авторизацию пользователя")
    def login_user_with_payload(payload: dict):
        login_payload = Payloads.request_login_payload()
        login_payload["email"] = payload["email"]
        login_payload["password"] = payload["password"]
        response = requests.post(Urls.AUTH_LOGIN_URL, json=login_payload)
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Изменить данные пользователя")
    def changing_user_data_payload(access_token: str):
        headers = {
            "Authorization": access_token
        }

        payload = Payloads.changing_user_data_payload()
        payload["email"] = f"{random_string()}@test.com"
        payload["name"] = random_string(6).capitalize()

        response = requests.patch(
            Urls.AUTH_USER_URL,
            headers=headers,
            json=payload
        )
        return response.status_code, response.json(), payload

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload: dict, access_token: str = None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        response = requests.post(
            Urls.ORDERS_URL,
            headers=headers,
            json=payload
        )

        try:
            body = response.json()
        except ValueError:
            body = response.text
        return response.status_code, body

    @staticmethod
    @allure.step("Получить заказы пользователя")
    def get_user_orders(access_token: str = None):
        headers = {}

        if access_token:
            headers["Authorization"] = access_token

        response = requests.get(
            Urls.ORDERS_URL,
            headers=headers
        )

        try:
            body = response.json()
        except ValueError:
            body = response.text

        return response.status_code, body
