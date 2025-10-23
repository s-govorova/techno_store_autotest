import datetime
from selenium.webdriver.common.keys import Keys


class BaseMethod:
    def __init__(self, driver):
        self.driver = driver

    def open_site(self, site_link):
        """Метод для перехода на сайт"""
        self.driver.get(site_link)

    def check_url(self):
        """Метод возвращает текущее url"""
        return self.driver.current_url

    def assert_text(self, webelement, word):
        """Метод принимает вебэлемент, у которого достает текст и проверочное слово. Данные сравниваются"""
        result_txt = webelement.text
        assert result_txt == word, f"Ожидали текст: {word}, но фактически получили текст: {result_txt}"
        return f'Ожидаемый результат текста: {word} = фактическому: {result_txt} '

    def click_webelement(self, webelement):
        webelement.click()

    def send_keys(self, webelement, data):
        webelement.send_keys(data)

    def click_key_enter(self, webelement):
        """Метод клика клавиши ENTER"""
        key = Keys()
        webelement.send_keys(key.ENTER)
