import pytest
from PageObjects.registration_user_page import RegistrationUserPage


@pytest.mark.parametrize('input_fields', ['input-firstname', 'input-lastname', 'input-email', 'input-telephone'])
@pytest.mark.personal_details_form
def test_personal_details_form(browser, base_url, input_fields):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_personal_details_form(input_fields)


@pytest.mark.parametrize('input_fields', ['input-password', 'input-confirm'])
@pytest.mark.password_form
def test_password_form(browser, base_url, input_fields):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_password_form(input_fields)


@pytest.mark.btns_subscribe
def test_btns_subscribe(browser, base_url):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_btns_subscribe()


@pytest.mark.privacy_policy_checkpoint
def test_privacy_policy_checkpoint(browser, base_url):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_privacy_policy_checkpoint()


@pytest.mark.btn_continue
def test_btn_continue(browser, base_url):
    reg_user_page = RegistrationUserPage(browser, base_url + '/index.php?route=account/register')
    reg_user_page.open()
    reg_user_page.should_be_btn_continue()


@pytest.mark.registration_new_user
def test_registration_new_user(browser, base_url):
    reg_user_page = RegistrationUserPage(browser, base_url)
    reg_user_page.open()
    reg_user_page.registration_new_user()
    reg_user_page.should_be_success_registration()
