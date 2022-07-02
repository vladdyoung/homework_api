import allure

from PageObjects.base_page import BasePage
from PageObjects.locators import CatalogLocators
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    @allure.step('Check all catalogs is present')
    def should_be_all_catalogs(self, list_of_products):
        try:
            self.logger.info(f'Find element {list_of_products}')
            self.is_element_present(*CatalogLocators.CATALOG)
            self.browser.find_element(*CatalogLocators.CATALOG).find_elements(By.LINK_TEXT, list_of_products)
        except:
            self.allure_attach()
            self.logger.error(f'Element ({list_of_products}) is not present')
            raise AssertionError(f'Element ({list_of_products}) is not present')
