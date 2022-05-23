import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.found_opencart_signature
def test_found_opencart_signature(browser, base_url):
    browser.get(base_url)
    by_opencart_signature = browser.find_element(By.CSS_SELECTOR, 'footer .container p a').text
    assert by_opencart_signature == 'OpenCart', 'OpenCart is not found'


@pytest.mark.search_line
def test_search_line(browser, base_url):
    browser.get(base_url)
    assert browser.find_element(By.ID, 'search'), 'Search line is not found'


@pytest.mark.bucket
def test_bucket(browser, base_url):
    browser.get(base_url)
    assert browser.find_element(By.ID, 'cart'), 'Bucket is not found'


@pytest.mark.swiper_wrapper_products
def test_swiper_wrapper_products(browser, base_url):
    browser.get(base_url)
    assert browser.find_element(By.CSS_SELECTOR, '#slideshow0 .swiper-wrapper')


@pytest.mark.macbook_air_poster_is_visibility
def test_macbook_air_poster_is_visibility(browser, base_url):
    browser.get(base_url)
    macbookair = WebDriverWait(browser, 3).until(EC.visibility_of_element_located
                                                 ((By.CSS_SELECTOR, '.swiper-slide-active [alt="MacBookAir"]')))
    assert macbookair, 'MackBookAir poster is not visible'


@pytest.mark.iphone6_poster_is_visibility
def test_iphone_poster_is_visibility(browser, base_url):
    browser.get(base_url)
    iphone6 = WebDriverWait(browser, 3).until(EC.visibility_of_element_located
                                                 ((By.CSS_SELECTOR, '.swiper-slide-active [alt="iPhone 6"]')))
    assert iphone6, 'Iphone6 poster is not visible'
