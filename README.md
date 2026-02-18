# Project_1
## Task_2
Задание 2 промежуточного проекта, 28_qa-python

```text
Task_2/
│── allure-results/                             # Отчёты Allure
│
├── data/
│   ├── data_requests.py                        # База запросов
│   ├── data_response.py                        # База ответов
│   └── data_urls.py                            # База URL
│
├── tests/
│   ├── test_changing_user_data_api.py          # Тесты на изменение данных пользователя
│   ├── test_create_order_api.py                # Тесты на создание заказа
│   ├── test_create_user_api.py                 # Тесты на создание пользователя
│   ├── test_login_user_api.py                  # Тесты на логин пользователя
│   └── test_receiving_orders_api.py            # Тесты на получение заказов конкретного пользователя
│
├── api_methods.py                              # Методы взаимодействия с api                     
├── conftest.py                                 # Фикстуры pytest
├── helpers.py                                  # Вспомогательная логика для тестов
├── requirements.txt                            # Подключённые библиотеки
└── README.md                                   # Описание проекта
