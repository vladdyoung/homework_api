import pytest
from PageObjects.main_page import MainPage


@pytest.mark.found_opencart_signature
def test_found_opencart_signature(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_opencart_signature()


@pytest.mark.search_line
def test_search_line(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_search_line()


@pytest.mark.bucket
def test_bucket(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_bucket()


@pytest.mark.swiper_wrapper_products
def test_swiper_wrapper_products(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_swiper_wrapper_products()


@pytest.mark.macbook_air_poster_is_visibility
def test_macbook_air_poster_is_visibility(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_macbook_air_poster_is_visibility()


@pytest.mark.iphone6_poster_is_visibility
def test_iphone_poster_is_visibility(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_iphone6_poster_is_visibility()
