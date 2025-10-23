from base.base_method import BaseMethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class ProductsPage(BaseMethod):
    SELECT_CATEGORY_TYPE = (By.CSS_SELECTOR, "#category")  # здесь библиотека Select
    SEARCH_TYPE = (By.CSS_SELECTOR, "#search")  # здесь input
    BUTTON_SEARCH = (By.CSS_SELECTOR, ".submit")  # здесь click
    TYPE_TITLE_PRODUCT = (By.CSS_SELECTOR, ".title")  # от того, что мы находим, может быть либо один товар, либо два
    BUTTON_ON_MAIN = (By.XPATH, "(//button[@role='button' and @class='main'])[1]")
    BUTTON_IN_CART = (By.XPATH, "(//input[@type='submit' and @class='cart'])[1]")
    CART = (By.XPATH, "// button[contains(text(), 'Корзина')]")
    NAME_PRODUCT = (By.XPATH, "(//p[@class='title']/a)[2]")
    NAME_PRODUCT_IN_CART = (By.XPATH, "//p[@class='title']/a")

    def get_select_category_product(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SELECT_CATEGORY_TYPE)
        )

    def get_search_product(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_TYPE)
        )

    def get_button_search(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_SEARCH)
        )

    def get_type_products(self):
        '''Здесь будем искать сразу списком, т.к товаров может быть > 1
        Если искомых товаров нет - вернем пустой список'''
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(self.TYPE_TITLE_PRODUCT)
            )
        except TimeoutException:
            return []

    def get_button_on_main(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_ON_MAIN)
        )

    def get_button_in_cart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_IN_CART)
        )

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART)
        )

    def get_name_product_main_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAME_PRODUCT)
        )

    def get_name_product_in_cart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAME_PRODUCT_IN_CART)
        )

    # actions
    def select_category_product(self):
        # выпадашку обработали - нашли тип камер - потом кликнули Поиск!
        self.open_site('http://localhost:8080/index')
        select_category = Select(self.get_select_category_product())
        select_category.select_by_visible_text("Camera")  # сразу кликает
        self.click_webelement(self.get_button_search())

    def input_name_product(self, product_name):
        '''Ввели с клавиатуры название продукта: кликнули Поиск!'''
        self.open_site('http://localhost:8080/index')
        self.send_keys(self.get_search_product(), product_name)
        self.click_webelement(self.get_button_search())

    def check_category_product(self):
        self.select_category_product()
        list_products_webelements = self.get_type_products()  # список вебэлементов
        for word in list_products_webelements:
            name_product = word.text.lower().split()
            if 'camera' in name_product:
                return True
        return False

    def check_filter_enter_query(self, input_name_product):
        self.input_name_product(input_name_product)
        list_products_webelements = self.get_type_products()  # список вебэлементов, либо пустой список, когда вводим несущ. продукт
        for word in list_products_webelements:
            name_product = word.text.lower().split()
            if input_name_product.lower() in name_product:
                return True
        return False

    def click_button_on_main(self):
        self.click_webelement(self.get_button_on_main())

    def click_button_in_cart(self):
        self.click_webelement(self.get_button_in_cart())

    def click_cart(self):
        self.click_webelement(self.get_cart())

    def text_name_product_main(self):
        return self.get_name_product_main_page().text.lower()

    def text_name_product_in_cart(self):
        return self.get_name_product_in_cart().text.lower()

    def add_product_in_cart(self):
        name_product_main_page = self.text_name_product_main()
        self.click_button_in_cart()
        self.click_cart()
        return name_product_main_page






