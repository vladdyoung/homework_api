from PageObjects.base_page import BasePage
from PageObjects.locators import AdminPageLocators


class AdminPage(BasePage):
    # def open_admin_page(self, base_url):
    #     self.admin_page = BasePage(self, base_url + '/admin')
    #     self.admin_page.open()

    def should_be_description_actions(self):
        assert self.is_element_present(*AdminPageLocators.DESCRIPTION_ACTIONS), 'Not description actions for admin'

    def should_be_user_name_field(self):
        assert self.is_element_present(*AdminPageLocators.USER_NAME), 'Not username field'

    def should_be_user_password_field(self):
        assert self.is_element_present(*AdminPageLocators.PASSWORD), 'Not password field'

    def should_be_halp_block(self):
        assert self.is_element_present(*AdminPageLocators.HELP_BLOCK), 'Not button for help'

    def should_be_btn_login(self):
        assert self.is_element_present(*AdminPageLocators.BTN_LOGIN), 'Not button for login'
