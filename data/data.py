user_data = {
    "valid": {
        "email": "test_user@yandex.ru",
        "password": "password123",
        "name": "Test User"
    },
    "missing_email": {
        "password": "password123",
        "name": "Test User"
    },
    "missing_password": {
        "email": "test_user@yandex.ru",
        "name": "Test User"
    },
    "missing_name": {
        "email": "test_user@yandex.ru",
        "password": "password123"
    }
}

login_data = {
    "wrong_password": {
        "email": "test_user@yandex.ru",
        "password": "wrongpass"
    }
}
