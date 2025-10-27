import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture()
def init_driver():
    """Фикстура для инициализации Chrome WebDriver"""
    chrome_driver_install = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=chrome_driver_install, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def authorization_user_driver(init_driver):
    '''Фикстура авторизованного пользователя, возвращает главную страницу'''
    lg = LoginPage(init_driver)
    lg.autorization_localhost("user@mail.com", "user")
    yield init_driver
    init_driver.quit()
