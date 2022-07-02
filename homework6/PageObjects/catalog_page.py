from PageObjects.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    def should_be_all_catalogs(self, list_of_products):
        assert self.browser.find_element(By.CSS_SELECTOR, '#column-left .list-group').find_elements\
            (By.PARTIAL_LINK_TEXT, list_of_products), f'Element {list_of_products} is not found'
