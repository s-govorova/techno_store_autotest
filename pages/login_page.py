from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_method import BaseMethod


class LoginPage(BaseMethod):
    # локаторы-константы
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON_SAVE = (By.CSS_SELECTOR, ".save")
    ERROR_MESSAGE = (By.XPATH, "//h3[contains(text(),'Invalid')]")
    TITLE_TECHNO_STORE = (By.XPATH, "//h2")

    # getters
    def get_login(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGIN_EMAIL)
        )

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD)
        )

    def get_button_save(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_SAVE)
        )

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )

    def get_title_techno_store(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE_TECHNO_STORE)
        )

    # actions
    def input_login(self, login):
        self.send_keys(self.get_login(), login)

    def input_password(self, password):
        self.send_keys(self.get_password(), password)

    def click_save(self):
        self.click_webelement(self.get_button_save())

    def autorization_localhost(self, login, password):
        self.open_site("http://localhost:8080/login")
        self.input_login(login)
        self.input_password(password)
        self.click_save()
