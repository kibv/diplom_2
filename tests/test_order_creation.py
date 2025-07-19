import allure
import requests
from data.urls import ORDERS_URL, INGREDIENTS_URL

@allure.feature("Создание и получение заказа")
class TestCreateGetOrders:
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, user_token):
        token = user_token["token"]
        assert token is not None, "No access token received after login"
        headers = {"Authorization": token}
        ingredients = requests.get(INGREDIENTS_URL).json()["data"]
        ingredient_ids = [i["_id"] for i in ingredients[:2]]
        res = requests.post(ORDERS_URL, json={"ingredients": ingredient_ids}, headers=headers)
        assert res.status_code == 200
        assert res.json()["order"]["ingredients"], "No ingredients found in order"

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        ingredients = requests.get(INGREDIENTS_URL).json()["data"]
        ingredient_ids = [i["_id"] for i in ingredients[:2]]
        res = requests.post(ORDERS_URL, json={"ingredients": ingredient_ids})
        assert res.status_code == 200
        assert res.json()["success"] is True
        assert "number" in res.json()["order"]

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, user_token):
        token = user_token["token"]
        assert token is not None, "No access token received after login"
        headers = {"Authorization": token}
        res = requests.post(ORDERS_URL, json={"ingredients": []}, headers=headers)
        assert res.status_code == 400

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(self, user_token):
        token = user_token["token"]
        assert token is not None, "No access token received after login"
        headers = {"Authorization": token}
        res = requests.post(ORDERS_URL, json={"ingredients": ["invalid_id"]}, headers=headers)
        assert res.status_code == 500

    @allure.title("Создание заказа без авторизации и без ингредиентов")
    def test_create_order_no_auth_no_ingredients(self):
        res = requests.post(ORDERS_URL, json={"ingredients": []})
        assert res.status_code == 400


