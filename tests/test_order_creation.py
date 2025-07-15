import allure
import requests
from data.urls import ORDERS_URL, INGREDIENTS_URL

@allure.feature("Order Creation and Retrieval")
class TestGetOrders:

    @allure.story("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, user_token):
        headers = {"Authorization": user_token["token"]}
        ingredients = requests.get(INGREDIENTS_URL).json()["data"]
        ingredient_ids = [i["_id"] for i in ingredients[:2]]
        res = requests.post(ORDERS_URL, json={"ingredients": ingredient_ids}, headers=headers)
        assert res.status_code == 200

    @allure.story("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        ingredients = requests.get(INGREDIENTS_URL).json()["data"]
        ingredient_ids = [i["_id"] for i in ingredients[:2]]
        res = requests.post(ORDERS_URL, json={"ingredients": ingredient_ids})
        assert res.status_code == 200

    @allure.story("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, user_token):
        headers = {"Authorization": user_token["token"]}
        res = requests.post(ORDERS_URL, json={"ingredients": []}, headers=headers)
        assert res.status_code == 400

    @allure.story("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(self, user_token):
        headers = {"Authorization": user_token["token"]}
        res = requests.post(ORDERS_URL, json={"ingredients": ["invalid_id"]}, headers=headers)
        assert res.status_code == 500

    @allure.story("Создание заказа без авторизации и без ингредиентов")
    def test_create_order_no_auth_no_ingredients(self):
        res = requests.post(ORDERS_URL, json={"ingredients": []})
        assert res.status_code == 400
        body = res.json()
        assert body["success"] is False


