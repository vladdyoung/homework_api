import pytest
from selenium.webdriver.common.by import By


@pytest.mark.images_of_product
def test_images_of_product(browser, base_url):
    browser.get(base_url + 'macbook')
    images = browser.find_elements(By.CSS_SELECTOR, '.thumbnails li')
    assert len(images) == 5, 'One or more images is not found'


@pytest.mark.parametrize('reference', ['Description', 'Specification', 'Reviews'])
@pytest.mark.references
def test_references(browser, base_url, reference):
    browser.get(base_url + 'macbook')
    references = browser.find_element(By.CSS_SELECTOR, '.nav.nav-tabs').\
        find_elements(By.PARTIAL_LINK_TEXT, f'{reference}')
    assert references, f'Reference {reference} is nod found'


@pytest.mark.name_product
def test_name_product(browser, base_url):
    browser.get(base_url + 'macbook')
    assert browser.find_element(By.CSS_SELECTOR, 'h1'), 'No name product'


@pytest.mark.description_product
def test_description_product(browser, base_url):
    browser.get(base_url + 'macbook')
    assert browser.find_elements(By.CSS_SELECTOR, '.col-sm-4 .list-unstyled')[0], 'No description product'


@pytest.mark.price_product
def test_price_product(browser, base_url):
    browser.get(base_url + 'macbook')
    assert browser.find_elements(By.CSS_SELECTOR, '.col-sm-4 .list-unstyled')[1], 'Price is not found'


@pytest.mark.btn_add_to_card
def test_btn_add_to_card(browser, base_url):
    browser.get(base_url + 'macbook')
    assert browser.find_element(By.CSS_SELECTOR, '#product button'), 'Button for add to cart is not found'
