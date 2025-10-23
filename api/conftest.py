import pytest
import requests


@pytest.fixture()
def public_products_list_object():
    """Возвращает ответ от публичной API ручки /external/products/findAll"""
    base_url = 'http://localhost:8080/external/products/findAll'
    return requests.get(base_url)