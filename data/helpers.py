import random
import requests
from data.urls import USER_URL
def get_random():
    return str(random.randint(10000,99999))

def delete_user(token: str):
    headers = {"Authorization": token}
    res = requests.delete(USER_URL, headers=headers)
    if res.status_code not in [200, 202]:
        raise Exception(f"Не удалось удалить пользователя: {res.status_code}, {res.text}")
    return res