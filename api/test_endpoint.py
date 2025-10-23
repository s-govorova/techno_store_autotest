import allure


@allure.title("Проверка статус-кода ответа публичного эндпоинта http://localhost:8080/external/products/findAll")
@allure.description("Проверяем, что сервер отвечает с кодом 200")
def test_status_code_response(public_products_list_object):
    r = public_products_list_object
    assert r.status_code == 200, f"Ожидался 200, а получен {r.status_code}"
    print(f"Статус-код ответа: {r.status_code}")


@allure.title("Проверка тела ответа публичного эндпоинта http://localhost:8080/external/products/findAll")
@allure.description("Проверяем, что ответ: список и в каждом объекте списка есть поле title")
def test_fields_response(public_products_list_object):
    response = public_products_list_object
    body_json_response = response.json()

    assert type(body_json_response) == list, f"Ошибка: ожидался тип list, получен {type(body_json_response)}"

    for item in body_json_response:
        assert "title" in item, "В теле ответа нет поля title"
        print("Поле 'title' найдено в объекте ответа")
