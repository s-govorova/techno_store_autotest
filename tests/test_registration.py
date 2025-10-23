from pages.registration_page import RegistrationPage
import allure

@allure.title('Регистрация нового пользователя')
@allure.description("""
Проверяем, что при заполнении формы регистрации корректными данными 
пользователь успешно создаётся и происходит редирект на страницу авторизации.
""")
def test_registration_new_user(init_driver):
    rp = RegistrationPage(init_driver)
    with allure.step('''Открываем страницу авторизации:
    1. Кликаем кнопку "Не зарегистрированы?
    2. Редирект на страницу регистрации: заполняем поля
    3. После заполнения полей кликаем кнопку: Регистрация
    4. Происходит редирект на страницу авторизации"'''):
        rp.registration_users()
    with allure.step('''Проверяем редирект после успешной регистрации на страницу авторизации'''):
        assert rp.check_url() == 'http://localhost:8080/login', 'После регистрации не открылась страница входа'
