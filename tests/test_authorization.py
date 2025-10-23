import pytest
from pages.login_page import LoginPage
import allure


@allure.title('Авторизация пользователя: валидные/невалидыне проверки')
@allure.description("""Проверяем авторизацию пользователя:
1. Уже зарегистрированного в системе
2. Незарегистрированного в системе
3. Проверяем авторизацию пустых полей: логин и пароля""")
@pytest.mark.parametrize(
    "login, password",
    [("user@mail.com", "user"), ("ashfahfh@asfa8427.org", "user"), (" ", " ")])
def test_authorization(init_driver, login, password):
    lg = LoginPage(init_driver)

    with allure.step("""
    1. Переходим на страницу авторизации
    2. Вводим логин и пароль
    3. Кликаем кнопку 'Войти'
    """):
        lg.autorization_localhost(login, password)

    if login == "user@mail.com" and password == "user":
        with allure.step("""
        Проверяем редирект на страницу выбора товаров после успешной авторизации:
        1. Находим элемент с названием магазина
        2. Сравниваем его текст
        """):
            lg.assert_text(lg.get_title_techno_store(), "techno store")

    elif (login == "ashfahfh@asfa8427.org" and password == "user") or (login == "" and password == ""):
        with allure.step("""
        Проверяем невалидные данные:
        1. Вводим неправильные или пустые поля
        2. Проверяем сообщение об ошибке
        """):
            lg.assert_text(
                lg.get_error_message(),
                "Invalid email address or password, or this account does not exist"
            )