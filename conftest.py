import pytest
import random
from data.urls import REGISTER_URL, LOGIN_URL, USER_URL
import requests

def get_random():
    return str(random.randint(10000,99999))


@pytest.fixture(scope="function")
def user_token():
    email = f"mail{get_random()}@yandex.ru"
    password = f"pass{get_random()}"
    name = f"name{get_random()}"

    # Регистрация
    res = requests.post(REGISTER_URL, json={
        "email": email,
        "password": password,
        "name": name
    })
    assert res.status_code == 200

    # Логин
    res_login = requests.post(LOGIN_URL, json={
        "email": email,
        "password": password
    })
    assert res_login.status_code == 200
    token = res_login.json()["accessToken"]

    yield {
        "token": token,
        "email": email,
        "password": password
    }

    # Удаление пользователя
    headers = {"Authorization": token}
    res_delete = requests.delete(USER_URL, headers=headers)
    assert res_delete.status_code in [200, 202]
