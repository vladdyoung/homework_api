import allure
from PageObjects.base_page import BasePage
from PageObjects.locators import *


class ProductPage(BasePage):
    @allure.step('Login')
    def login(self):
        self.is_element_present(*AdminPageLocators.USER_NAME), 'Element is not found'
        self.logger.info('Enter user name')
        user_name = self.browser.find_element(*AdminPageLocators.USER_NAME)
        user_name.clear()
        user_name.click()
        user_name.send_keys('user')
        self.is_element_present(*AdminPageLocators.PASSWORD), 'Element is not found'
        password = self.browser.find_element(*AdminPageLocators.PASSWORD)
        self.logger.info('Enter user password')
        password.clear()
        password.click()
        password.send_keys('bitnami')
        self.is_element_present(*AdminPageLocators.BTN_LOGIN), 'Element is not found'
        self.browser.find_element(*AdminPageLocators.BTN_LOGIN).click()

    @allure.step('Add new product')
    def add_new_product(self):
        try:
            self.is_element_present(*ProductPageLocators.CATALOG_REF), 'Element is not found'
            self.logger.info('Click catalog reference')
            catalog_reference = self.browser.find_element(*ProductPageLocators.CATALOG_REF).click()
            self.is_element_present(*ProductPageLocators.PRODUCTS_CATEGORY), 'Element is not found'
            self.logger.info('Choose product category')
            product_reference = self.browser.find_elements(*ProductPageLocators.PRODUCTS_CATEGORY)[1].click()
            self.is_element_present(*ProductPageLocators.BTN_ADD_NEW_PRODUCT), 'Element is not found'
            self.logger.info('Click btn add new product')
            btn_add_new_product = self.browser.find_element(*ProductPageLocators.BTN_ADD_NEW_PRODUCT).click()
            self.is_element_present(*AddProductPageLocators.GENERAL_TAB), 'Element is not found'
            self.logger.info('Click general tab')
            general_tab = self.browser.find_element(*AddProductPageLocators.GENERAL_TAB).click()
            self.is_element_present(*AddProductPageLocators.PRODUCT_NAME), 'Element is not found'
            self.logger.info('Enter product name')
            product_name = self.browser.find_element(*AddProductPageLocators.PRODUCT_NAME)
            product_name.clear()
            product_name.click()
            product_name.send_keys('Example Product')
            self.is_element_present(*AddProductPageLocators.META_TEG_TITLE), 'Element is not found'
            self.logger.info('Enter meta teg title')
            meta_tag_title = self.browser.find_element(*AddProductPageLocators.META_TEG_TITLE)
            meta_tag_title.clear()
            meta_tag_title.click()
            meta_tag_title.send_keys('Example Meta Tag')
            self.is_element_present(*AddProductPageLocators.DATA_TAB), 'Element is not found'
            self.logger.info('Click data tab')
            data_tab = self.browser.find_element(*AddProductPageLocators.DATA_TAB).click()
            self.is_element_present(*AddProductPageLocators.MODEL), 'Element is not found'
            self.logger.info('Enter model')
            model = self.browser.find_element(*AddProductPageLocators.MODEL)
            model.clear()
            model.click()
            model.send_keys('Example Model')
            self.is_element_present(*AddProductPageLocators.BTN_SAVE), 'Element is not found'
            self.logger.info('Click btn save')
            btn_save = self.browser.find_element(*AddProductPageLocators.BTN_SAVE).click()
        except:
            self.allure_attach()
            self.logger.error('Product not added')
            raise AssertionError('Product not added')

    @allure.step('Delete product')
    def del_product(self):
        try:
            self.is_element_present(*ProductPageLocators.CATALOG_REF), 'Element is not found'
            self.logger.info('Click on catalog reference')
            catalog_reference = self.browser.find_element(*ProductPageLocators.CATALOG_REF).click()
            self.is_element_present(*ProductPageLocators.PRODUCTS_CATEGORY), 'Element is not found'
            self.logger.info('Choose product category')
            product_reference = self.browser.find_elements(*ProductPageLocators.PRODUCTS_CATEGORY)[1].click()
            self.is_element_present(*DelProductPageLocator.CHECKBOX_PRODUCT), 'Element is not found'
            self.logger.info('Choose product')
            checkbox_product = self.browser.find_element(*DelProductPageLocator.CHECKBOX_PRODUCT).click()
            self.is_element_present(*DelProductPageLocator.BTN_DELETE), 'Element is not found'
            self.logger.info('Delete product')
            btn_delete = self.browser.find_element(*DelProductPageLocator.BTN_DELETE).click()
        except:
            self.allure_attach()
            self.logger.error('Product not deleted')
            raise AssertionError('Product not deleted')

    @allure.step('Check that login is success')
    def should_be_success_login(self):
        try:
            self.is_element_present(*ProductPageLocators.MENU)
            self.logger.info('Login successfully')
        except:
            self.allure_attach()
            self.logger.error('You are not login')
            raise AssertionError('You are not login')

    @allure.step('Check product add is success')
    def should_be_success_massage(self):
        try:
            self.logger.info('Check that the product was added')
            self.is_element_present(*ProductPageLocators.SUCCESS_MASSAGE)
            self.logger.info('Product add successfully')
        except:
            self.allure_attach()
            self.logger.error('Product not added')
            raise AssertionError('Product not added')
