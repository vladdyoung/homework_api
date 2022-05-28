from PageObjects.base_page import BasePage
from PageObjects.locators import CurrencyLocators


def should_be_match_currency(old_currency, new_currency):
    assert old_currency != new_currency, 'Currency not change!'


class Currency(BasePage):
    def change_currency_on_dollar(self):
        current_currency = self.browser.find_element(*CurrencyLocators.CURRENT_CURRENCY).text
        btn_currency = self.browser.find_element(*CurrencyLocators.BTN_CURRENCY).click()
        us_dollar = self.browser.find_element(*CurrencyLocators.EURO).click()
        new_currency = self.browser.find_element(*CurrencyLocators.NEW_CURRENCY).text
        should_be_match_currency(current_currency, new_currency)

