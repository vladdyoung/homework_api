import pytest
from PageObjects.currency import Currency


@pytest.mark.currency_toggle
def test_currency_toggle(browser, base_url):
    currency = Currency(browser, base_url)
    currency.open()
    currency.change_currency_on_dollar()
