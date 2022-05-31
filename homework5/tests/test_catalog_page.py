"""Для примера сделал проверку восьми элементов каталога в одном тесте"""

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('list_of_products', ['Desktops', 'Laptops & Notebooks',
                                              'Components', 'Tablets', 'Software',
                                              'Phones & PDAs', 'Cameras', 'MP3 Players'])
def test_all_catalog(browser, base_url, list_of_products):
    browser.get(base_url + '/desktops')
    assert browser.find_element(By.CSS_SELECTOR, '#column-left .list-group').find_elements\
        (By.PARTIAL_LINK_TEXT, f'{list_of_products}'), f'Element {list_of_products} is not found'
