import allure
from PageObjects.base_page import BasePage
from PageObjects.locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    @allure.step('Check opencart signature is present')
    def should_be_opencart_signature(self):
        try:
            self.logger.info(f'Find element {MainPageLocators.OPENCART_SIGNATURE[1]} '
                             f'by using {MainPageLocators.OPENCART_SIGNATURE[0]}')
            self.is_element_present(*MainPageLocators.OPENCART_SIGNATURE)
            equals = self.browser.find_element(*MainPageLocators.OPENCART_SIGNATURE).text == 'OpenCart'
        except:
            self.allure_attach()
            self.logger.error('OpenCart is not found')
            raise AssertionError('OpenCart is not found')

    @allure.step('Check search line is present')
    def should_be_search_line(self):
        try:
            self.logger.info(f'Find element {MainPageLocators.SEARCH_LINE[1]} '
                             f'by using {MainPageLocators.SEARCH_LINE[0]}')
            self.is_element_present(*MainPageLocators.SEARCH_LINE)
        except:
            self.allure_attach()
            self.logger.error('Search line is not found')
            raise AssertionError('Search line is not found')

    @allure.step('Check bucket is present')
    def should_be_bucket(self):
        try:
            self.logger.info(f'Find element {MainPageLocators.BUCKET[1]} '
                             f'by using {MainPageLocators.BUCKET[0]}')
            self.is_element_present(*MainPageLocators.BUCKET)
        except:
            self.allure_attach()
            self.logger.error('Bucket is not found')
            raise AssertionError('Bucket is not found')

    @allure.step('Check swiper wrapper products is present')
    def should_be_swiper_wrapper_products(self):
        try:
            self.logger.info(f'Find element {MainPageLocators.SWIPER_WRAPPER_PRODUCTS[1]} '
                             f'by using {MainPageLocators.SWIPER_WRAPPER_PRODUCTS[0]}')
            self.is_element_present(*MainPageLocators.SWIPER_WRAPPER_PRODUCTS)
        except:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name=type(self).__name__,
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error('Change panel is not found')
            raise AssertionError('Change panel is not found')

    @allure.step('Check macbook air poster is visibility')
    def should_be_macbook_air_poster_is_visibility(self):
        try:
            self.logger.info(f'Wait for {MainPageLocators.MACBOOK_AIR_POSTER[1]} to appear')
            macbookair = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located
                                                             (MainPageLocators.MACBOOK_AIR_POSTER))
        except:
            self.allure_attach()
            self.logger.error('MackBookAir poster is not visible')
            raise AssertionError('MackBookAir poster is not visible')

    @allure.step('Check iphone6 poster is visibility is visibility')
    def should_be_iphone6_poster_is_visibility(self):
        try:
            self.logger.info(f'Wait for {MainPageLocators.IPHONE6_POSTER[1]} to appear')
            iphone6 = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located
                                                           (MainPageLocators.IPHONE6_POSTER))
        except:
            self.allure_attach()
            self.logger.error('Iphone6 poster is not visible')
            raise AssertionError('Iphone6 poster is not visible')
