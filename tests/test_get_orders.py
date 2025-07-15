import allure
import requests
from data.urls import ORDERS_URL

@allure.feature("Get Orders")
class TestGetOrders:

    @allure.story("Получение заказов авторизованного пользователя")
    def test_get_orders_authorized(self, user_token):
        headers = {"Authorization": user_token["token"]}
        res = requests.get(ORDERS_URL, headers=headers)
        assert res.status_code == 200
        body = res.json()
        assert body["success"] is True
        assert isinstance(body["orders"], list)

    @allure.story("Получение заказов без авторизации")
    def test_get_orders_unauthorized(self):
        res = requests.get(ORDERS_URL)
        assert res.status_code == 401
        body = res.json()
        assert body["success"] is False
        assert "authorised" in body["message"]
