import pytest
from selenium.webdriver.common.by import By


@pytest.mark.description_actions
def test_description_actions(browser, base_url):
    browser.get(base_url + 'admin')
    assert browser.find_element(By.CSS_SELECTOR, '.panel-heading'), 'Not description actions for admin'


@pytest.mark.username_field
def test_username_field(browser, base_url):
    browser.get(base_url + 'admin')
    assert browser.find_element(By.CSS_SELECTOR, '#input-username'), 'Not username field'


@pytest.mark.password_field
def test_password_field(browser, base_url):
    browser.get(base_url + 'admin')
    assert browser.find_element(By.CSS_SELECTOR, '#input-password'), 'Not password field'


@pytest.mark.halp_block
def test_halp_block(browser, base_url):
    browser.get(base_url + 'admin')
    assert browser.find_element(By.CSS_SELECTOR, '.help-block'), 'Not button for halp'


@pytest.mark.btn_login
def test_btn_login(browser, base_url):
    browser.get(base_url + 'admin')
    assert browser.find_element(By.CSS_SELECTOR, 'button'), 'Not button for login'
