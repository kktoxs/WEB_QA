import random
import time

from conftest import BASE_URL
from pages.base_page import BasePage
from locators.auth_page_locators import AuthPageLocators as Locators


class AuthPage(BasePage):
    url = BASE_URL  # + '/auth'

    def __init__(self, driver):
        super().__init__(driver, self.url)
        super(AuthPage, self).open()  # страницы авторизации автоматически открываются при создании

    def sign_in_with_mail(self, email, password):
        self.element(Locators.TOP_CORNER_SIGN_IN_BUTTON).click()
        self.elements(Locators.SIGN_BUTTONS)[0].click()
        time.sleep(1)
        self.element(Locators.EMAIL_SWITCH).click()
        time.sleep(1)
        self.element(Locators.LOGIN_INPUT).send_keys(email)
        self.element(Locators.PASSWORD_INPUT).send_keys(password)
        self.element(Locators.CONTINUE_BUTTON).click()
        time.sleep(1)

    def register_with_mail(self, email, password, confirm_password):
        self.element(Locators.TOP_CORNER_SIGN_IN_BUTTON).click()
        self.elements(Locators.SIGN_BUTTONS)[1].click()
        time.sleep(1)
        self.element(Locators.EMAIL_SWITCH).click()
        time.sleep(1)
        self.element(Locators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.element(Locators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.element(Locators.REGISTER_PASSWORD_CONFIRM_INPUT).send_keys(confirm_password)
        self.element(Locators.CONTINUE_BUTTON).click()

    def sign_in_with_phone(self, phone):
        self.element(Locators.TOP_CORNER_SIGN_IN_BUTTON).click()
        self.elements(Locators.SIGN_BUTTONS)[1].click()
        self.element(Locators.PHONE_NUMBER_INPUT).send_keys(phone)
        self.element(Locators.CONTINUE_BUTTON).click()

    def get_error_message(self):
        return self.element(Locators.ERROR_MESSAGE).text

    def get_register_error_message(self):
        return self.element(Locators.REGISTER_ERROR_MESSAGE).text

    def reset_password(self, email):
        self.element(Locators.RESET_PASSWORD_BUTTON).click()
        time.sleep(1)
        self.element(Locators.EMAIL_SWITCH).click()
        self.element(Locators.RESET_EMAIL_INPUT).send_keys(email)
        #  self.element(Locators.RESET_PASSWORD_SEND_CODE_BUTTON).click()  жду пока исправят задвоение блока

    def get_reset_error_message(self):
        return self.element(Locators.RESET_PASSWORD_ERROR_MESSAGE).text

    def send_random_code(self):
        random_code = random.randint(1000,9999)
        self.element(Locators.PHONE_CODE_INPUT).send_keys(random_code)

    def submit(self):
        self.element(Locators.CONTINUE_BUTTON).click()
