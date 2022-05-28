import pytest
from PageObjects.admin_page import AdminPage


@pytest.mark.description_actions
def test_description_actions(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_description_actions()


@pytest.mark.username_field
def test_username_field(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_user_name_field()


@pytest.mark.password_field
def test_password_field(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_user_password_field()


@pytest.mark.halp_block
def test_halp_block(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_halp_block()


@pytest.mark.btn_login
def test_btn_login(browser, base_url):
    page_admin = AdminPage(browser, base_url + 'admin')
    page_admin.open()
    page_admin.should_be_btn_login()
