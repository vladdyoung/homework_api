from PageObjects.base_page import BasePage
from PageObjects.locators import *


class ProductPage(BasePage):
    def login(self):
        user_name = self.browser.find_element(*AdminPageLocators.USER_NAME)
        user_name.clear()
        user_name.click()
        user_name.send_keys('user')
        password = self.browser.find_element(*AdminPageLocators.PASSWORD)
        password.clear()
        password.click()
        password.send_keys('bitnami')
        self.browser.find_element(*AdminPageLocators.BTN_LOGIN).click()

    def add_new_product(self):
        catalog_reference = self.browser.find_element(*ProductPageLocators.CATALOG_REF).click()
        product_reference = self.browser.find_elements(*ProductPageLocators.PRODUCTS_CATEGORY)[1].click()
        btn_add_new_product = self.browser.find_element(*ProductPageLocators.BTN_ADD_NEW_PRODUCT).click()
        general_tab = self.browser.find_element(*AddProductPageLocators.GENERAL_TAB).click()
        product_name = self.browser.find_element(*AddProductPageLocators.PRODUCT_NAME)
        product_name.clear()
        product_name.click()
        product_name.send_keys('Example Product')
        meta_tag_title = self.browser.find_element(*AddProductPageLocators.META_TEG_TITLE)
        meta_tag_title.clear()
        meta_tag_title.click()
        meta_tag_title.send_keys('Example Meta Tag')
        data_tab = self.browser.find_element(*AddProductPageLocators.DATA_TAB).click()
        model = self.browser.find_element(*AddProductPageLocators.MODEL)
        model.clear()
        model.click()
        model.send_keys('Example Model')
        btn_save = self.browser.find_element(*AddProductPageLocators.BTN_SAVE).click()

    def del_product(self):
        catalog_reference = self.browser.find_element(*ProductPageLocators.CATALOG_REF).click()
        product_reference = self.browser.find_elements(*ProductPageLocators.PRODUCTS_CATEGORY)[1].click()
        checkbox_product = self.browser.find_element(*DelProductPageLocator.CHECKBOX_PRODUCT).click()
        btn_delete = self.browser.find_element(*DelProductPageLocator.BTN_DELETE).click()

    def should_be_success_login(self):
        assert self.is_element_present(*ProductPageLocators.MENU), 'You are not login'

    def should_be_success_massage(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MASSAGE), 'Not done'
