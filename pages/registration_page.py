from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_method import BaseMethod
from faker import Faker


class RegistrationPage(BaseMethod):
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, ".button")
    EMAIL = (By.CSS_SELECTOR, "#email")
    NAME = (By.CSS_SELECTOR, "#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#lastname")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON_SAVE = (By.CSS_SELECTOR, ".save")

    # getters
    def get_button_registration(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_REGISTRATION)
        )

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL)
        )

    def get_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAME)
        )

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD)
        )

    def get_button_save(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_SAVE)
        )

    # actions
    def click_registration_button(self):
        self.click_webelement(self.get_button_registration())

    def input_email(self, email):
        self.send_keys(self.get_email(), email)

    def input_name(self, name):
        self.send_keys(self.get_name(), name)

    def input_last_name(self, last_name):
        self.send_keys(self.get_last_name(), last_name)

    def input_password(self, password):
        self.send_keys(self.get_password(), password)

    def click_save(self):
        self.click_webelement(self.get_button_save())

    # methods
    def registration_users(self):
        faker = Faker("en_US")
        self.open_site('http://localhost:8080/login')
        self.click_registration_button()
        self.input_email(faker.email())
        self.input_name(faker.first_name())
        self.input_last_name(faker.last_name())
        self.input_password(faker.password())
        self.click_save()

