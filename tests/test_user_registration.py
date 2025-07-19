import pytest
import allure
import requests
import random
from data.urls import REGISTER_URL
from data.data import user_data
from data.helpers import delete_user

@allure.feature("User Registration")
class TestUserRegistration:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        payload = user_data["valid"].copy()
        payload["email"] = f"unique_{random.randint(10000,99999)}@yandex.ru"
        res = requests.post(REGISTER_URL, json=payload)
        assert res.status_code == 200
        body = res.json()
        assert body["success"] is True
        assert body["user"]["email"] == payload["email"]
        assert body["user"]["name"] == payload["name"]
        token = body.get("accessToken")
        assert token is not None, "No token returned"
        delete_user(token)


    @allure.title("Создание уже существующего пользователя")
    def test_create_existing_user(self, user_token):
        register_res = user_token["register_response"]
        assert register_res.status_code == 200, f"Registration failed: {register_res.text}"
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

    @allure.title("Создание пользователя без email")
    def test_create_user_missing_email(self):
        payload = user_data["missing_email"]
        res = requests.post(REGISTER_URL, json=payload)
        assert res.status_code == 403
        body = res.json()
        assert body["success"] is False
        assert "required fields" in body["message"]

    @allure.title("Создание пользователя без пароля")
    def test_create_user_missing_password(self):
        payload = user_data["missing_password"]
        payload["email"] = f"no_pass_{random.randint(10000,99999)}@yandex.ru"
        res = requests.post(REGISTER_URL, json=payload)
        assert res.status_code == 403
        body = res.json()
        assert body["success"] is False
        assert "required fields" in body["message"]

    @allure.title("Создание пользователя без имени")
    def test_create_user_missing_name(self):
        payload = user_data["missing_name"]
        payload["email"] = f"no_name_{random.randint(10000,99999)}@yandex.ru"
        res = requests.post(REGISTER_URL, json=payload)
        assert res.status_code == 403
        body = res.json()
        assert body["success"] is False
        assert "required fields" in body["message"]
