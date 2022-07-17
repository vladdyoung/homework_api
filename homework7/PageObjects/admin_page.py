import allure
from PageObjects.base_page import BasePage
from PageObjects.locators import AdminPageLocators


class AdminPage(BasePage):
    @allure.step('Check description actions is present')
    def should_be_description_actions(self):
        try:
            self.logger.info(f'Find element ({AdminPageLocators.DESCRIPTION_ACTIONS[1]}) '
                             f'by using ({AdminPageLocators.DESCRIPTION_ACTIONS[0]})')
            self.is_element_present(*AdminPageLocators.DESCRIPTION_ACTIONS)
        except:
            self.allure_attach()
            self.logger.error('Not description actions for admin')
            raise AssertionError('Not description actions for admin')

    @allure.step('Check username field is present')
    def should_be_user_name_field(self):
        try:
            self.logger.info(f'Find element ({AdminPageLocators.USER_NAME[1]}) '
                             f'by using ({AdminPageLocators.USER_NAME[0]})')
            self.is_element_present(*AdminPageLocators.USER_NAME)
        except:
            self.allure_attach()
            self.logger.error('Not username field')
            raise AssertionError('Not username field')

    @allure.step('Check user password field is present')
    def should_be_user_password_field(self):
        try:
            self.logger.info(f'Find element ({AdminPageLocators.PASSWORD[1]}) '
                             f'by using ({AdminPageLocators.PASSWORD[0]})')
            self.is_element_present(*AdminPageLocators.PASSWORD)
        except:
            self.allure_attach()
            self.logger.error('Not password field')
            raise AssertionError('Not password field')

    @allure.step('Check halp block is present')
    def should_be_halp_block(self):
        try:
            self.logger.info(f'Find element ({AdminPageLocators.HELP_BLOCK[1]}) '
                             f'by using ({AdminPageLocators.HELP_BLOCK[0]})')
            self.is_element_present(*AdminPageLocators.HELP_BLOCK)
        except:
            self.allure_attach()
            self.logger.error('Not button for help')
            raise AssertionError('Not button for help')

    @allure.step('Check login button is present')
    def should_be_btn_login(self):
        try:
            self.logger.info(f'Find element ({AdminPageLocators.BTN_LOGIN[1]}) '
                             f'by using ({AdminPageLocators.BTN_LOGIN[0]})')
            self.is_element_present(*AdminPageLocators.BTN_LOGIN)
        except:
            self.allure_attach()
            self.logger.error('Not button for login')
            raise AssertionError('Not button for help')
