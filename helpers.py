import random
import string
from data.data_requests import Payloads

def random_string(length=8): # Генерируем случайные буквы
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_payload(): # Генерируем случайные email, password, name для создания юзера
    data = Payloads.request_create_user_payload()
    data["email"] = f"{random_string()}@test.com"
    data["password"] = random_string(12)
    data["name"] = random_string(6).capitalize()
    return data
