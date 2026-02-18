BASE_URL = "https://stellarburgers.education-services.ru/"

class ApiEndpoints:
    AUTH_REGISTER_ENDPOINT = "api/auth/register" # Создание/регистрация пользователя
    AUTH_USER_ENDPOINT = "api/auth/user" # Удаление пользователя
    AUTH_LOGIN_ENDPOINT = "api/auth/login" # Авторизация пользователя
    ORDERS_ENDPOINT = "api/orders" # Заказы
    INGREDIENTS_ENDPOINT = "api/ingredients" # Ингредиенты

class Urls:
    AUTH_REGISTER_URL = BASE_URL + ApiEndpoints.AUTH_REGISTER_ENDPOINT # api/auth/register
    AUTH_USER_URL = BASE_URL + ApiEndpoints.AUTH_USER_ENDPOINT # api/auth/user
    AUTH_LOGIN_URL = BASE_URL + ApiEndpoints.AUTH_LOGIN_ENDPOINT # api/auth/login
    ORDERS_URL = BASE_URL + ApiEndpoints.ORDERS_ENDPOINT # api/orders
    INGREDIENTS_URL = BASE_URL + ApiEndpoints.INGREDIENTS_ENDPOINT # api/ingredients
