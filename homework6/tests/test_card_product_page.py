import pytest
from PageObjects.card_product_page import CardProductPage


@pytest.mark.images_of_product
def test_images_of_product(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_five_images()


@pytest.mark.parametrize('reference', ['Description', 'Specification', 'Reviews'])
@pytest.mark.references
def test_references(browser, base_url, reference):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_references(reference)


@pytest.mark.name_product
def test_name_product(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_name_product()


@pytest.mark.description_product
def test_description_product(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_description_product()


@pytest.mark.price_product
def test_price_product(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_price_product()


@pytest.mark.btn_add_to_card
def test_btn_add_to_card(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_btn_add_to_card()
