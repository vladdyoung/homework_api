import allure
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from PageObjects.locators import CardProductPageLocators


class CardProductPage(BasePage):
    @allure.step('Check images is present')
    def should_be_five_images(self):
        try:
            self.logger.info(f'Find element ({CardProductPageLocators.IMAGES_PRODUCT[1]}) '
                             f'by using method ({CardProductPageLocators.IMAGES_PRODUCT[0]})')
            self.is_element_present(*CardProductPageLocators.IMAGES_PRODUCT)
            length = len(self.browser.find_elements(*CardProductPageLocators.IMAGES_PRODUCT)) == 5
        except:
            self.allure_attach()
            self.logger.error('One or more images is not found')
            raise AssertionError('One or more images is not found')

    @allure.step('Check reference is present')
    def should_be_references(self, reference):
        try:
            self.logger.info(f'Find element {CardProductPageLocators.REFERENCES[1]} '
                             f'by using method {CardProductPageLocators.REFERENCES[0]}')
            self.is_element_present(*CardProductPageLocators.REFERENCES)
            self.browser.find_element(*CardProductPageLocators.REFERENCES)\
                .find_elements(By.PARTIAL_LINK_TEXT, reference)
        except:
            self.allure_attach()
            self.logger.error('Reference is not found')
            raise AssertionError('Reference is not found')

    @allure.step('Check name product is present')
    def should_be_name_product(self):
        try:
            self.logger.info(f'Find element ({CardProductPageLocators.NAME_PRODUCT[1]}) '
                             f'by using method ({CardProductPageLocators.NAME_PRODUCT[0]})')
            self.is_element_present(*CardProductPageLocators.NAME_PRODUCT)
        except:
            self.allure_attach()
            self.logger.error('No name product')
            raise AssertionError('No name product')

    @allure.step('Check description product is present')
    def should_be_description_product(self):
        try:
            self.logger.info(f'Find element ({CardProductPageLocators.PROPERTY_PRODUCT})')
            self.browser.find_elements(*CardProductPageLocators.PROPERTY_PRODUCT)[0]
        except:
            self.allure_attach()
            self.logger.error('No description product')
            raise AssertionError('No description product')

    @allure.step('Check price product is present')
    def should_be_price_product(self):
        try:
            self.logger.info(f'Find element ({CardProductPageLocators.PROPERTY_PRODUCT})')
            self.browser.find_elements(*CardProductPageLocators.PROPERTY_PRODUCT)[1]
        except:
            self.allure_attach()
            self.logger.error('Price is not found')
            raise AssertionError('Price is not found')

    @allure.step('Check button add to card is present')
    def should_be_btn_add_to_card(self):
        try:
            self.logger.info(f'Find element ({CardProductPageLocators.BTN_ADD_TO_CARD[1]}) '
                         f'by using method ({CardProductPageLocators.BTN_ADD_TO_CARD[0]})')
            self.is_element_present(*CardProductPageLocators.BTN_ADD_TO_CARD)
        except:
            self.allure_attach()
            self.logger.error('Button for add to cart is not found')
            raise AssertionError('Button for add to cart is not found')
