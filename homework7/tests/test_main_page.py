import pytest
import allure
from PageObjects.main_page import MainPage


@allure.step('Test found opencart signature')
@allure.feature('Main page')
@allure.title('Test found opencart signature')
@pytest.mark.found_opencart_signature
def test_found_opencart_signature(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_opencart_signature()


@allure.step('Test search line is present')
@allure.feature('Main page')
@allure.title('Test search line is present')
@pytest.mark.search_line
def test_search_line(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_search_line()


@allure.step('Test bucket is present')
@allure.feature('Main page')
@allure.title('Test bucket is present')
@pytest.mark.bucket
def test_bucket(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_bucket()


@allure.step('Test swiper wrapper products is present')
@allure.feature('Main page')
@allure.title('Test swiper wrapper products is present')
@pytest.mark.swiper_wrapper_products
def test_swiper_wrapper_products(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_swiper_wrapper_products()


@allure.step('Test macbook air poster is visibility')
@allure.feature('Main page')
@allure.title('Test macbook air poster is visibility')
@pytest.mark.macbook_air_poster_is_visibility
def test_macbook_air_poster_is_visibility(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_macbook_air_poster_is_visibility()


@allure.step('Test iphone6 poster is visibility')
@allure.feature('Main page')
@allure.title('Test iphone6 poster is visibility')
@pytest.mark.iphone6_poster_is_visibility
def test_iphone_poster_is_visibility(browser, base_url):
    main_page = MainPage(browser, base_url)
    main_page.open()
    main_page.should_be_iphone6_poster_is_visibility()
