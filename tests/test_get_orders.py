import allure
import requests
from data.urls import ORDERS_URL

@allure.feature("Получение заказа")
class TestGetOrders:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_authorized(self, user_token):
        token = user_token["token"]
        assert token is not None, "No access token received after login"
        headers = {"Authorization": token}
        res = requests.get(ORDERS_URL, headers=headers)
        assert res.status_code == 200
        body = res.json()
        assert body["success"] is True
        assert isinstance(body["orders"], list)

    @allure.title("Получение заказов без авторизации")
    def test_get_orders_unauthorized(self):
        res = requests.get(ORDERS_URL)
        assert res.status_code == 401
        body = res.json()
        assert body["success"] is False
        assert "authorised" in body["message"]
