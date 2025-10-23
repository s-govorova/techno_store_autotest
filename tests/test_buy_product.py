import pytest
import allure
from pages.products_page import ProductsPage


@allure.title("Проверка фильтрации товаров по категории 'Camera'")
@allure.description("""
Проверяем фильтрацию товаров по категории 'Camera' (через выпадающий список).
Если найдена хотя бы одна камера — тест проходит.
""")
def test_filter_camera_category(authorization_user_driver):
    pp = ProductsPage(authorization_user_driver)

    with allure.step("Открываем главную страницу и выбираем категорию из выпадающего спика - 'Camera'"):
        result_filter = pp.check_category_product()
        assert result_filter, 'Фильтр по категории "Camera" ничего не нашел'

    with allure.step("Кликаем на кнопку: 'На главную': редирект на главную страницу"):
        pp.click_button_on_main()
        assert pp.check_url() == 'http://localhost:8080/index', 'Ошибка: нет редиректа на главную страницу'


@allure.title("Проверка поиска товаров по вводимому названию в поле 'Запрос'")
@allure.description("""
Проверяем фильтрацию по названию товара:
1. Вводим 'Lenovo': товар должен быть найден.
2. Вводим 'Books': товар отсутствует, отображается пустой результат.
""")
@pytest.mark.parametrize("name_product", ["Lenovo", "Books"])
def test_filter_enter_query(authorization_user_driver, name_product):
    pp = ProductsPage(authorization_user_driver)

    if name_product == "Lenovo":
        with allure.step(f"Вводим запрос 'Lenovo' и проверяем, что товар найден"):
            assert pp.check_filter_enter_query(name_product), f"После фильтрации по запросу {name_product}товары не найдены"

        with allure.step("Переходим на главную страницу и проверяем редирект"):
            pp.click_button_on_main()
            assert pp.check_url() == 'http://localhost:8080/index', 'Ошибка: редиректа на главную страницу нет'

    elif name_product == "Books":
        with allure.step(f"Вводим запрос 'Books' и проверяем, что товар отсутствует"):
            assert not pp.check_filter_enter_query(name_product), f"Фильтрация по запросу {name_product} не должна возвращать товары"

        with allure.step("Переходим на главную страницу и проверяем редирект"):
            pp.click_button_on_main()
            assert pp.check_url() == 'http://localhost:8080/index', 'Ошибка: редиректа на главную страницу нет'


@allure.title("Добавление товара в корзину")
@allure.description("""
Проверяем добавление товара в корзину:
1. На главной странице выбираем товар:Apple iPhone 13 128 ГБ Black.
2. Проверяем что его название совпадает с тем, что добавилось в корзину.
""")
def test_add_product_in_cart(authorization_user_driver):
    pp = ProductsPage(authorization_user_driver)

    with allure.step("Добавляем товар в корзину, сохраняем название товара до редиректа в корзину"):
        name_product_on_main_page = pp.add_product_in_cart()

    with allure.step("Проверяем, что выбранный товар совпадает с тем, что в корзине"):
        name_product_in_cart = pp.text_name_product_in_cart()
        assert name_product_on_main_page == name_product_in_cart, 'Ошибка: название товаров не совпадают'
