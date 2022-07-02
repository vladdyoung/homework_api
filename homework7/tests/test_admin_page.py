import allure
import pytest
from PageObjects.admin_page import AdminPage


@allure.step('Test that description actions is present')
@allure.feature('Admin page')
@allure.title('Test that description actions is present')
@pytest.mark.description_actions
def test_description_actions(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_description_actions()


@allure.step('Test that username field is present')
@allure.feature('Admin page')
@allure.title('Test that username field is present')
@pytest.mark.username_field
def test_username_field(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_user_name_field()


@allure.step('Test that password is present')
@allure.feature('Admin page')
@allure.title('Test that password is present')
@pytest.mark.password_field
def test_password_field(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_user_password_field()


@allure.step('Test that halp block is present')
@allure.feature('Admin page')
@allure.title('Test that halp block is present')
@pytest.mark.halp_block
def test_help_block(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_halp_block()


@allure.step('Test that login button is present')
@allure.feature('Admin page')
@allure.title('Test that login button is present')
@pytest.mark.btn_login
def test_btn_login(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_btn_login()
