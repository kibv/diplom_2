import pytest
import allure
import requests
from data.urls import USER_URL
import random

@allure.feature("User Update")
class TestUserUpdate:

    @allure.story("Изменение данных с авторизацией")
    @pytest.mark.parametrize("field,value", [
        ("name", "NewName"),
        ("email", f"updated_{random.randint(10000,99999)}@example.com")
    ])
    def test_update_user_authorized(self, user_token, field, value):
        headers = {"Authorization": user_token["token"]}
        res = requests.patch(USER_URL, json={field: value}, headers=headers)
        assert res.status_code == 200
        body = res.json()
        assert body["success"] is True
        assert body["user"][field] == value

    @allure.story("Изменение данных без авторизации")
    def test_update_user_unauthorized(self):
        res = requests.patch(USER_URL, json={"name": "NoAuth"})
        assert res.status_code == 401
        body = res.json()
        assert body["success"] is False
        assert "authorised" in body["message"]
