class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/"

class ApiEndpoints:
    CREATE_USER_ENDPOINT = "api/auth/register" # Создание/регистрация пользователя
    DELETE_USER_ENDPOINT = "api/auth/user" # Удаление пользователя
    LOGIN_ENDPOINT = "api/auth/login" # Авторизация пользователя

class TotalUrl:
    TOTAL_CREATE_USER_URL = Urls.BASE_URL + ApiEndpoints.CREATE_USER_ENDPOINT # Создаем юзера
    TOTAL_DELETE_USER_URL = Urls.BASE_URL + ApiEndpoints.DELETE_USER_ENDPOINT # Удаляем юзера
    TOTAL_LOGIN_URL = Urls.BASE_URL + ApiEndpoints.LOGIN_ENDPOINT # Проходим авторизацию
