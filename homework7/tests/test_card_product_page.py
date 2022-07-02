import allure
import pytest
from PageObjects.card_product_page import CardProductPage


@allure.step('Test images of product is present')
@allure.feature('Card product page')
@allure.title('Test images of product is present')
@pytest.mark.images_of_product
def test_images_of_product(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_five_images()


@allure.step('Test references is present')
@allure.feature('Card product page')
@allure.title('Test references is present')
@pytest.mark.parametrize('reference', ['Description', 'Specification', 'Reviews'])
@pytest.mark.references
def test_references(browser, base_url, reference):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_references(reference)


@allure.step('Test name product is present')
@allure.feature('Card product page')
@allure.title('Test name product is present')
@pytest.mark.name_product
def test_name_product(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_name_product()


@allure.step('Test description product is present')
@allure.feature('Card product page')
@allure.title('Test description product is present')
@pytest.mark.description_product
def test_description_product(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_description_product()


@allure.step('Test price product is present')
@allure.feature('Card product page')
@allure.title('Test price product is present')
@pytest.mark.price_product
def test_price_product(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_price_product()


@allure.step('Test button add to card is present')
@allure.feature('Card product page')
@allure.title('Test button add to card is present')
@pytest.mark.btn_add_to_card
def test_btn_add_to_card(browser, base_url):
    card_product_page = CardProductPage(browser, base_url + 'macbook')
    card_product_page.open()
    card_product_page.should_be_btn_add_to_card()
