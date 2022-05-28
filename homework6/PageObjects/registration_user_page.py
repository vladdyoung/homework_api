from PageObjects.base_page import BasePage
from PageObjects.locators import *


class RegistrationUserPage(BasePage):
    def registration_new_user(self):
        dropdown_for_reg = self.browser.find_element(*RegistrationPageLocators.DROPDOWN_FOR_REG).click()
        btn_registration = self.browser.find_element(*RegistrationPageLocators.BTN_REGISTRATION).click()
        first_name = self.browser.find_element(*RegistrationPageLocators.FIRST_NAME)
        first_name.clear()
        first_name.click()
        first_name.send_keys('Имя')
        last_name = self.browser.find_element(*RegistrationPageLocators.LAST_NAME)
        last_name.clear()
        last_name.click()
        last_name.send_keys('Фамилия')
        e_mail = self.browser.find_element(*RegistrationPageLocators.TELEPHONE)
        e_mail.clear()
        e_mail.click()
        e_mail.send_keys('mail@mail.ru')
        telephone = self.browser.find_element(*RegistrationPageLocators.TELEPHONE)
        telephone.clear()
        telephone.click()
        telephone.send_keys('888888888')
        password = self.browser.find_element(*RegistrationPageLocators.PASSWORD)
        password.clear()
        password.click()
        password.send_keys('Pass')
        password_confirm = self.browser.find_element(*RegistrationPageLocators.PASSWORD)
        password_confirm.clear()
        password_confirm.click()
        password_confirm.send_keys('Pass')
        checkbox_privacy = self.browser.find_element(*RegistrationPageLocators.CHECKBOX_PRIVACY).click()
        btn_continue = self.browser.find_element(*RegistrationPageLocators.BTN_CONTINUE).click()

    def should_be_btns_subscribe(self):
        assert self.browser.find_elements(*RegistrationUserLocators.BTNS_SUBSCRIBE[0])[2]\
            .find_elements(*RegistrationUserLocators.BTNS_SUBSCRIBE[1]), \
            'Buttons of subscribe is not found'

    def should_be_privacy_policy_checkpoint(self):
        assert self.is_element_present(*RegistrationUserLocators.PRIVACY_POLICY_CHECKPOINT), 'Checkbox is not found'

    def should_be_btn_continue(self):
        assert self.is_element_present(*RegistrationUserLocators.BTN_CONTINUE), 'Continue button is not found'

    def should_be_personal_details_form(self, input_fields):
        assert self.browser.find_elements(By.CSS_SELECTOR, '#' + input_fields), \
            'Not field ' + input_fields[6:].title()

    def should_be_password_form(self, input_fields):
        assert self.browser.find_elements(By.CSS_SELECTOR, '#' + input_fields), \
            'Not field ' + input_fields[6:].title()

    def should_be_success_registration(self):
        message = self.browser.find_element(*RegistrationPageLocators.SUCCESS_MASSAGE)
        assert message.text == 'Register Account', 'Fail registration'
