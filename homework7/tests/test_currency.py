import allure
import pytest
from PageObjects.currency import Currency


@allure.step('Test change currency')
@allure.feature('Currency')
@allure.title('Test change currency')
@pytest.mark.currency_toggle
def test_currency_toggle(browser, base_url):
    currency = Currency(browser, base_url)
    currency.open()
    currency.change_currency_on_dollar()
