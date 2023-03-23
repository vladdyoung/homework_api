import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('input_fields', ['input-firstname', 'input-lastname', 'input-email', 'input-telephone'])
@pytest.mark.personal_details_form
def test_personal_details_form(browser, input_fields):
    browser.get('http://localhost/index.php?route=account/register')
    fields = browser.find_elements(By.CSS_SELECTOR, f'#{input_fields}')
    assert fields, 'Not field ' + f'{input_fields}'[6:].title()


@pytest.mark.parametrize('input_fields', ['input-password', 'input-confirm'])
@pytest.mark.password_form
def test_password_form(browser, input_fields):
    browser.get('http://localhost/index.php?route=account/register')
    fields = browser.find_elements(By.CSS_SELECTOR, f'#{input_fields}')
    assert fields, 'Not field ' + f'{input_fields}'[6:].title()


@pytest.mark.btns_subscribe
def test_btns_subscribe(browser):
    browser.get('http://localhost/index.php?route=account/register')
    assert browser.find_elements(By.CSS_SELECTOR, 'fieldset')[2].find_elements(By.CSS_SELECTOR, '.col-sm-10'), \
        'Buttons of subscribe is not found'


@pytest.mark.privacy_policy_checkpoint
def test_privacy_policy_checkpoint(browser):
    browser.get('http://localhost/index.php?route=account/register')
    assert browser.find_element(By.CSS_SELECTOR, '[type=checkbox]'), 'Checkbox is not found'


@pytest.mark.btn_continue
def test_btn_continue(browser):
    browser.get('http://localhost/index.php?route=account/register')
    assert browser.find_element(By.CSS_SELECTOR, '[type=submit]'), 'Continue button is not found'
