import pytest
import allure
import requests
import random
from data.urls import REGISTER_URL
from data.data import user_data

@allure.feature("User Registration")
class TestUserRegistration:

    @allure.story("Создание уникального пользователя")
    def test_create_unique_user(self):
        payload = user_data["valid"].copy()
        payload["email"] = f"unique_{random.randint(10000,99999)}@yandex.ru"
        res = requests.post(REGISTER_URL, json=payload)
        assert res.status_code == 200
        body = res.json()
        assert body["success"] is True
        assert body["user"]["email"] == payload["email"]
        assert body["user"]["name"] == payload["name"]

    @allure.story("Создание уже существующего пользователя")
    def test_create_existing_user(self, user_token):
        payload = {
            "email": user_token["email"],
            "password": user_token["password"],
            "name": "Duplicate User"
        }
        res = requests.post(REGISTER_URL, json=payload)
        assert res.status_code == 403
        body = res.json()
        assert body["success"] is False
        assert body["message"] == "User already exists"

    @allure.story("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["missing_email", "missing_password", "missing_name"])
    def test_create_user_missing_field(self, missing_field):
        payload = user_data[missing_field]
        if "email" in payload:
            payload = payload.copy()
            payload["email"] = f"missing_{random.randint(10000,99999)}@yandex.ru"

        res = requests.post(REGISTER_URL, json=payload)
        assert res.status_code == 403
        body = res.json()
        assert body["success"] is False
        assert "required fields" in body["message"]
