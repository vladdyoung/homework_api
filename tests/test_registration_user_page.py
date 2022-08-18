import pytest
import allure
from PageObjects.registration_user_page import RegistrationUserPage


@allure.step('Test personal details form is present')
@allure.feature('Registration user page')
@allure.title('Test personal details form is present')
@pytest.mark.parametrize('input_fields', ['input-firstname', 'input-lastname', 'input-email', 'input-telephone'])
@pytest.mark.personal_details_form
def test_personal_details_form(browser, base_url, input_fields):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_personal_details_form(input_fields)


@allure.step('Test password form is present')
@allure.feature('Registration user page')
@allure.title('Test password form is present')
@pytest.mark.parametrize('input_fields', ['input-password', 'input-confirm'])
@pytest.mark.password_form
def test_password_form(browser, base_url, input_fields):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_password_form(input_fields)


@allure.step('Test subscribe buttons is present')
@allure.feature('Registration user page')
@allure.title('Test subscribe buttons is present')
@pytest.mark.btns_subscribe
def test_btns_subscribe(browser, base_url):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_btns_subscribe()


@allure.step('Test privacy policy checkpoint is present')
@allure.feature('Registration user page')
@allure.title('Test privacy policy checkpoint is present')
@pytest.mark.privacy_policy_checkpoint
def test_privacy_policy_checkpoint(browser, base_url):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_privacy_policy_checkpoint()


@allure.step('Test continue button is present')
@allure.feature('Registration user page')
@allure.title('Test continue button is present')
@pytest.mark.btn_continue
def test_btn_continue(browser, base_url):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_btn_continue()


@allure.step('Test registration new user')
@allure.feature('Registration user page')
@allure.title('Test registration new user')
@pytest.mark.registration_new_user
def test_registration_new_user(browser, base_url):
    reg_user_page = RegistrationUserPage(browser, base_url)
    reg_user_page.open()
    reg_user_page.registration_new_user()
    reg_user_page.should_be_success_registration()
