from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from PageObjects.locators import CardProductPageLocators


class CardProductPage(BasePage):
    def should_be_five_images(self):
        assert len(self.browser.find_elements(*CardProductPageLocators.IMAGES_PRODUCT)) \
               == 5, 'One or more images is not found'

    def should_be_references(self, reference):
        assert self.browser.find_element(By.CSS_SELECTOR, '.nav.nav-tabs').\
            find_elements(By.PARTIAL_LINK_TEXT, reference), f'Reference {reference} is nod found'

    def should_be_name_product(self):
        assert self.is_element_present(*CardProductPageLocators.NAME_PRODUCT), 'No name product'

    def should_be_description_product(self):
        assert self.browser.find_elements(*CardProductPageLocators.PROPERTY_PRODUCT)[0], 'No description product'

    def should_be_price_product(self):
        assert self.browser.find_elements(*CardProductPageLocators.PROPERTY_PRODUCT)[1], 'Price is not found'

    def should_be_btn_add_to_card(self):
        assert self.is_element_present(*CardProductPageLocators.BTN_ADD_TO_CARD), 'Button for add to cart is not found'
