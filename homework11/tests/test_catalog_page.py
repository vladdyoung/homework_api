import pytest
import allure
from PageObjects.catalog_page import CatalogPage


@allure.step('Test all catalog is present')
@allure.feature('Catalog page')
@allure.title('Test all catalog is present')
@pytest.mark.parametrize('list_of_products', ['Desktops', 'Laptops & Notebooks',
                                              'Components', 'Tablets', 'Software',
                                              'Phones & PDAs', 'Cameras', 'MP3 Players'])
def test_all_catalogs(browser, base_url, list_of_products):
    catalog_page = CatalogPage(browser, base_url + '/desktops')
    catalog_page.open()
    catalog_page.should_be_all_catalogs(list_of_products)
