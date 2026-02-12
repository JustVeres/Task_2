import allure
from api_methods import UserApiMethods

"""Создание заказа"""

@allure.title("Создание заказа с авторизацией")
def test_create_order_with_auth(authorized_user, valid_ingredients, payload_order):
    _, token = authorized_user

    with allure.step("Подготовить корректное тело заказа"):
        payload_order["ingredients"] = valid_ingredients

    with allure.step("Отправить запрос с токеном авторизации"):
        status, body = UserApiMethods.create_order(payload_order, token)

    with allure.step("Проверить успешное создание заказа"):
        assert status == 200
        assert body["success"] is True
        assert "order" in body

@allure.title("Создание заказа без авторизации")
def test_create_order_without_auth(valid_ingredients, payload_order):

    with allure.step("Сформировать корректное тело заказа"):
        payload_order["ingredients"] = valid_ingredients

    with allure.step("Отправить запрос без токена"):
        status, body = UserApiMethods.create_order(payload_order)

    with allure.step("Проверить успешное создание заказа"):
        assert status == 200
        assert body["success"] is True

@allure.title("Создание заказа без ингредиентов")
def test_create_order_without_ingredients(payload_order):

    with allure.step("Отправить запрос"):
        status, body = UserApiMethods.create_order(payload_order)

    with allure.step("Проверить ошибку"):
        assert status == 400
        assert body["success"] is False
        assert body["message"] == "Ingredient ids must be provided"

@allure.title("Создание заказа с неверным хешем ингредиентов")
def test_create_order_with_invalid_hash(payload_order):
    with allure.step("Сформировать тело заказа с некорректным хешем"):
        payload_order["ingredients"] = ["invalid_hash_123"]

    with allure.step("Отправить запрос"):
        status, body = UserApiMethods.create_order(payload_order)

    with allure.step("Проверить ошибку сервера"):
        assert status == 500
