import requests
import allure
from helpers import generate_registration_payload
from data.data_requests import Payloads
from data.data_urls import TotalUrl

class UserApiMethods:

    @staticmethod
    @allure.step("Создать/зарегистрировать пользователя")
    def create_user_response():
        response = requests.post(TotalUrl.TOTAL_CREATE_USER_URL, json=generate_registration_payload())
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Удалить пользователя")
    def delete_user_response(access_token: str):
        headers = {"Authorization": access_token}
        response = requests.delete(TotalUrl.TOTAL_DELETE_USER_URL, headers=headers)
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Создать существующего пользователя")
    def create_user_with_payload(payload: dict):
        response = requests.post(TotalUrl.TOTAL_CREATE_USER_URL, json=payload)
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Выполнить авторизацию пользователя")
    def login_user_with_payload(payload: dict):
        login_payload = Payloads.request_login_payload()
        login_payload["email"] = payload["email"]
        login_payload["password"] = payload["password"]
        response = requests.post(TotalUrl.TOTAL_LOGIN_URL, json=login_payload)
        return response.status_code, response.json()


status, body = UserApiMethods.create_user_response()
print(status, body)
token = body["accessToken"]
print(UserApiMethods.delete_user_response(token))
