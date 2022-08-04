import time

from pages.base_page import BasePage
from locators.auth_page_locators import AuthPageLocators as Locators


class AuthPage(BasePage):
    url = 'https://planetfor.me/auth'

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def sign_in_with_mail(self, email, password):
        self.element(Locators.TOP_CORNER_SIGN_IN_BUTTON).click()
        self.element(Locators.SIGN_IN_BUTTON).click()
        self.element(Locators.EMAIL_SWITCH).click()
        self.element(Locators.LOGIN_INPUT).send_keys(email)
        self.element(Locators.PASSWORD_INPUT).send_keys(password)
        # self.element(Locators.CONTINUE_BUTTON).click()

    def submit(self):
        self.element(Locators.CONTINUE_BUTTON).click()

    def get_error_message(self):
        return self.element(Locators.ERROR_MESSAGE).text

    def reset_password(self, email):
        self.element(Locators.RESET_PASSWORD_BUTTON).click()
        time.sleep(1)
        self.element(Locators.EMAIL_SWITCH).click()
        self.element(Locators.RESET_EMAIL_INPUT).send_keys(email)
        #  self.element(Locators.RESET_PASSWORD_SEND_CODE_BUTTON).click()  жду пока исправят задвоение блока
