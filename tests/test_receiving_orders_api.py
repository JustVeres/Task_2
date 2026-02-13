import allure
from api_methods import UserApiMethods
from data.data_response import ErrorMessage as EM

"""Получение заказов конкретного пользователя"""

@allure.title("Получение заказов авторизованным пользователем")
def test_get_orders_authorized_user(authorized_user, valid_ingredients, payload_order):
    _, token = authorized_user

    with allure.step("Создать заказ для пользователя"):
        payload_order["ingredients"] = valid_ingredients
        UserApiMethods.create_order(payload_order, token)

    with allure.step("Отправить запрос на получение заказов пользователя"):
        status, body = UserApiMethods.get_user_orders(token)

    with allure.step("Проверить статус ответа"):
        assert status == 200

    with allure.step("Проверить структуру ответа"):
        assert body["success"] is True
        assert isinstance(body["orders"], list)
        assert "total" in body
        assert "totalToday" in body

    with allure.step("Проверить структуру одного заказа"):
        order = body["orders"][0]
        assert "ingredients" in order
        assert "_id" in order
        assert "status" in order
        assert "number" in order
        assert "createdAt" in order
        assert "updatedAt" in order

@allure.title("Получение заказов без авторизации")
def test_get_orders_unauthorized_user():

    with allure.step("Отправить запрос без токена"):
        status, body = UserApiMethods.get_user_orders()

    with allure.step("Проверить статус ошибки"):
        assert status == 401

    with allure.step("Проверить сообщение об ошибке"):
        assert body["success"] is False
        assert body["message"] == EM.SHOULD_BE_AUTHORISED_MESSAGE
