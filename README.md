Описание тестов: 

test_create_unique_user	- Создание уникального пользователя
test_create_existing_user	- Попытка создать пользователя с уже существующим email
test_create_user_missing_field	- Попытка создать пользователя без обязательного поля (email, password или name)

test_login_success	- Успешный вход под существующим пользователем
test_login_invalid_credentials	- Попытка входа с некорректными данными (неверный логин/пароль)

test_update_user_authorized	- Изменение данных авторизованным пользователем (email и name)
test_update_user_unauthorized	- Попытка изменить данные без авторизации

test_create_order_with_auth	- Создание заказа авторизованным пользователем
test_create_order_without_auth	- Создание заказа без авторизации
test_create_order_no_ingredients	- Попытка создать заказ без ингредиентов
test_create_order_invalid_ingredients	- Попытка создать заказ с невалидными id ингредиентов
test_create_order_no_auth_no_ingredients	- Попытка создать заказ без авторизации и без ингредиентов

test_get_orders_authorized -  Получение заказов авторизованным пользователем
test_get_orders_unauthorized	- Попытка получить заказы без авторизации