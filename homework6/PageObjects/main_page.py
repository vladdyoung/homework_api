from PageObjects.base_page import BasePage
from PageObjects.locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def should_be_opencart_signature(self):
        assert self.browser.find_element(*MainPageLocators.OPENCART_SIGNATURE).text\
               == 'OpenCart', 'OpenCart is not found'

    def should_be_search_line(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_LINE), 'Search line is not found'

    def should_be_bucket(self):
        assert self.is_element_present(*MainPageLocators.BUCKET), 'Bucket is not found'

    def should_be_swiper_wrapper_products(self):
        assert self.is_element_present(*MainPageLocators.SWIPER_WRAPPER_PRODUCTS), 'Change panel is not found'

    def should_be_macbook_air_poster_is_visibility(self):
        mabookair = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located
                                                     ((MainPageLocators.MACBOOK_AIR_POSTER)))
        assert mabookair, 'MackBookAir poster is not visible'

    def should_be_iphone6_poster_is_visibility(self):
        iphone6 = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located
                                                  ((MainPageLocators.IPHONE6_POSTER)))
        assert iphone6, 'Iphone6 poster is not visible'
