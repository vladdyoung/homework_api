import allure

from PageObjects.base_page import BasePage
from PageObjects.locators import CurrencyLocators


class Currency(BasePage):
    @allure.step('Check change currency')
    def change_currency_on_dollar(self):
        try:
            self.logger.info(f'Find element {CurrencyLocators.CURRENT_CURRENCY}')
            self.is_element_present(*CurrencyLocators.CURRENT_CURRENCY)
            old_currency = self.browser.find_element(*CurrencyLocators.CURRENT_CURRENCY).text
            self.logger.info(f'Find element {CurrencyLocators.BTN_CURRENCY}')
            self.is_element_present(*CurrencyLocators.BTN_CURRENCY)
            btn_currency = self.browser.find_element(*CurrencyLocators.BTN_CURRENCY).click()
            self.logger.info(f'Find element {CurrencyLocators.EURO}')
            self.is_element_present(*CurrencyLocators.EURO)
            euro = self.browser.find_element(*CurrencyLocators.EURO).click()
            self.is_element_present(*CurrencyLocators.NEW_CURRENCY)
            new_currency = self.browser.find_element(*CurrencyLocators.NEW_CURRENCY).text
            self.should_be_match_currency(old_currency, new_currency)
        except:
            self.allure_attach()
            self.logger.error('Currency is not change!')
            raise AssertionError('Currency is not change!')

    def should_be_match_currency(self, old_currency, new_currency):
        try:
            self.logger.info('Check currency change')
            equals = old_currency != new_currency
        except:
            self.allure_attach()
            self.logger.error('Currency is not change!')
            raise AssertionError('Currency is not change!')
