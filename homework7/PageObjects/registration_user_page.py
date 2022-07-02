import allure
from PageObjects.base_page import BasePage
from PageObjects.locators import *


class RegistrationUserPage(BasePage):
    @allure.step('Check registration new user')
    def registration_new_user(self):
        self.is_element_present(*RegistrationPageLocators.DROPDOWN_FOR_REG)
        self.logger.info('Click on dropdown for registration')
        dropdown_for_reg = self.browser.find_element(*RegistrationPageLocators.DROPDOWN_FOR_REG).click()
        self.is_element_present(*RegistrationPageLocators.BTN_REGISTRATION)
        self.logger.info('Click on button for registration')
        btn_registration = self.browser.find_element(*RegistrationPageLocators.BTN_REGISTRATION).click()
        self.is_element_present(*RegistrationPageLocators.FIRST_NAME)
        self.logger.info('Enter first name')
        first_name = self.browser.find_element(*RegistrationPageLocators.FIRST_NAME)
        first_name.clear()
        first_name.click()
        first_name.send_keys('Имя')
        self.is_element_present(*RegistrationPageLocators.LAST_NAME)
        self.logger.info('Enter last name')
        last_name = self.browser.find_element(*RegistrationPageLocators.LAST_NAME)
        last_name.clear()
        last_name.click()
        last_name.send_keys('Фамилия')
        self.is_element_present(*RegistrationPageLocators.E_MAIL)
        e_mail = self.browser.find_element(*RegistrationPageLocators.E_MAIL)
        self.logger.info('Enter e-mail')
        e_mail.clear()
        e_mail.click()
        e_mail.send_keys('mail@mail.ru')
        self.is_element_present(*RegistrationPageLocators.TELEPHONE)
        telephone = self.browser.find_element(*RegistrationPageLocators.TELEPHONE)
        self.logger.info('Enter telephone')
        telephone.clear()
        telephone.click()
        telephone.send_keys('888888888')
        self.is_element_present(*RegistrationPageLocators.PASSWORD)
        password = self.browser.find_element(*RegistrationPageLocators.PASSWORD)
        self.logger.info('Enter password')
        password.clear()
        password.click()
        password.send_keys('Pass')
        password_confirm = self.browser.find_element(*RegistrationPageLocators.PASSWORD)
        self.logger.info('Enter password for confirm')
        password_confirm.clear()
        password_confirm.click()
        password_confirm.send_keys('Pass')
        self.is_element_present(*RegistrationPageLocators.CHECKBOX_PRIVACY)
        checkbox_privacy = self.browser.find_element(*RegistrationPageLocators.CHECKBOX_PRIVACY).click()
        self.logger.info('Click on privacy checkbox')
        self.is_element_present(*RegistrationPageLocators.BTN_CONTINUE)
        btn_continue = self.browser.find_element(*RegistrationPageLocators.BTN_CONTINUE).click()

    @allure.step('Check buttons subscribe is present')
    def should_be_btns_subscribe(self):
        try:
            self.logger.info('Find element')
            self.browser.find_elements(*RegistrationUserLocators.BTNS_SUBSCRIBE[0])[2] \
                .find_elements(*RegistrationUserLocators.BTNS_SUBSCRIBE[1])
        except:
            self.allure_attach()
            self.logger.error('Buttons of subscribe is not found')
            raise AssertionError('Buttons of subscribe is not found')

    @allure.step('Check buttons subscribe is present')
    def should_be_privacy_policy_checkpoint(self):
        try:
            self.logger.info(f'Find {RegistrationUserLocators.PRIVACY_POLICY_CHECKPOINT[1]} '
                             f'by using {RegistrationUserLocators.PRIVACY_POLICY_CHECKPOINT[0]}')
            self.is_element_present(*RegistrationUserLocators.PRIVACY_POLICY_CHECKPOINT)
        except:
            self.allure_attach()
            self.logger.error('Checkbox is not found')
            raise AssertionError('Checkbox is not found')

    @allure.step('Check continue button is present')
    def should_be_btn_continue(self):
        try:
            self.logger.info(f'Find {RegistrationUserLocators.BTN_CONTINUE[1]} '
                             f'by using {RegistrationUserLocators.BTN_CONTINUE[0]}')
            self.is_element_present(*RegistrationUserLocators.BTN_CONTINUE)
        except:
            self.allure_attach()
            self.logger.error('Continue button is not found')
            raise AssertionError('Continue button is not found')

    @allure.step('Check personal details form is present')
    def should_be_personal_details_form(self, input_fields):
        try:
            self.logger.info(f'Find  #{input_fields} by using {By.CSS_SELECTOR}')
            self.browser.find_elements(By.CSS_SELECTOR, '#' + input_fields)
        except:
            self.allure_attach()
            self.logger.error('Not field ' + input_fields[6:].title())
            raise AssertionError('Not field ' + input_fields[6:].title())

    @allure.step('Check password form is present')
    def should_be_password_form(self, input_fields):
        try:
            self.logger.info(f'Find  #{input_fields} by using {By.CSS_SELECTOR}')
            self.browser.find_elements(By.CSS_SELECTOR, '#' + input_fields)
        except:
            self.allure_attach()
            self.logger.error('Not field ' + input_fields[6:].title())
            raise AssertionError('Not field ' + input_fields[6:].title())

    @allure.step('Check success registration')
    def should_be_success_registration(self):
        try:
            self.logger.info(f'Find {RegistrationPageLocators.SUCCESS_MASSAGE[1]} '
                             f'by using {RegistrationPageLocators.SUCCESS_MASSAGE[0]}')
            message = self.browser.find_element(*RegistrationPageLocators.SUCCESS_MASSAGE).text == 'Register Account'
            self.logger.info('User registration is successfully')
        except:
            self.allure_attach()
            self.logger.error('Fail registration')
            raise AssertionError('Fail registration')
