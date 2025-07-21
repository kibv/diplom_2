import pytest
from data.urls import REGISTER_URL, LOGIN_URL, USER_URL
import requests
from data.helpers import get_random
# @pytest.fixture(scope="function")
# def user_token():
#     email = f"mail{get_random()}@yandex.ru"
#     password = f"pass{get_random()}"
#     name = f"name{get_random()}"
#
#     # Регистрация
#     res = requests.post(REGISTER_URL, json={
#         "email": email,
#         "password": password,
#         "name": name
#     })
#     assert res.status_code == 200
#
#     # Логин
#     res_login = requests.post(LOGIN_URL, json={
#         "email": email,
#         "password": password
#     })
#     assert res_login.status_code == 200
#     token = res_login.json()["accessToken"]
#
#     yield {
#         "token": token,
#         "email": email,
#         "password": password
#     }
#
#     # Удаление пользователя
#     headers = {"Authorization": token}
#     res_delete = requests.delete(USER_URL, headers=headers)
#     assert res_delete.status_code in [200, 202]

import requests
from data.urls import REGISTER_URL, LOGIN_URL, USER_URL

@pytest.fixture(scope="function")
def user_token():
    email = f"mail{get_random()}@yandex.ru"
    password = f"pass{get_random()}"
    name = f"name{get_random()}"

    res_register = requests.post(REGISTER_URL, json={
        "email": email,
        "password": password,
        "name": name
    })

    res_login = requests.post(LOGIN_URL, json={
        "email": email,
        "password": password
    })

    token = None
    if res_login.status_code == 200 and "accessToken" in res_login.json():
        token = res_login.json()["accessToken"]

    yield {
        "email": email,
        "password": password,
        "register_response": res_register,
        "login_response": res_login,
        "token": token,
    }

    if token:
        headers = {"Authorization": token}
        requests.delete(USER_URL, headers=headers)
