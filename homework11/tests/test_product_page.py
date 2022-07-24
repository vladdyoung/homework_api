import pytest
import allure
from PageObjects.product_page import ProductPage


@allure.step('Test add new product')
@allure.feature('Product page')
@allure.title('Add new product')
@pytest.mark.add_product
def test_add_product(browser, base_url):
    """
    Проверка добавления нового продукта в магазин.
    1. Переход в админку
    2. Логин
    3. Проверка успешности входа в систему
    4. Добавление нового продукта
    5. Проверка успешности добавления продукта
    """
    product_page = ProductPage(browser, base_url + '/admin')
    product_page.open()
    product_page.login()
    product_page.should_be_success_login()
    product_page.add_new_product()
    product_page.should_be_success_massage()


@allure.step
@allure.feature('Product page')
@allure.title('Delete product')
@pytest.mark.delete_product
def test_delete_product(browser, base_url):
    """
    Проверка удаления продукта в магазин.
    1. Переход в админку
    2. Логин
    3. Проверка успешности входа в систему
    4. Удаление продукта
    5. Проверка успешности удаления продукта
    """
    product_page = ProductPage(browser, base_url + '/admin')
    product_page.open()
    product_page.login()
    product_page.should_be_success_login()
    product_page.del_product()
