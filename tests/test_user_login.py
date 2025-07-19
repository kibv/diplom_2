import pytest
import allure
import requests
from data.urls import LOGIN_URL
import random

@allure.feature("User Login")
class TestUserLogin:

    @allure.title("Успешный логин под существующим пользователем")
    def test_login_success(self, user_token):
        login_res = user_token["login_response"]
        assert login_res.status_code == 200, f"Login failed: {login_res.text}"

        payload = {
            "email": user_token["email"],
            "password": user_token["password"]
        }
        res = requests.post(LOGIN_URL, json=payload)
        assert res.status_code == 200
        body = res.json()
        assert body["success"] is True
        assert "accessToken" in body

    @allure.title("Логин с неверными данными")
    def test_login_invalid_credentials(self):
        payload = {
            "email": f"nonexistent_{random.randint(10000,99999)}@yandex.ru",
            "password": "wrongpassword"
        }
        res = requests.post(LOGIN_URL, json=payload)
        assert res.status_code == 401
        body = res.json()
        assert body["success"] is False
        assert "incorrect" in body["message"]
