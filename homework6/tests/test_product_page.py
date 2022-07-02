import pytest
from PageObjects.product_page import ProductPage


@pytest.mark.add_product
def test_add_product(browser, base_url):
    product_page = ProductPage(browser, base_url + '/admin')
    product_page.open()
    product_page.login()
    product_page.should_be_success_login()
    product_page.add_new_product()
    product_page.should_be_success_massage()


@pytest.mark.delete_product
def test_delete_product(browser, base_url):
    product_page = ProductPage(browser, base_url + '/admin')
    product_page.open()
    product_page.login()
    product_page.should_be_success_login()
    product_page.del_product()
