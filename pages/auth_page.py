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

    def top_corner_sign_in_button_click(self):
        self.element(Locators.TOP_CORNER_SIGN_IN_BUTTON).click()
        time.sleep(1)

    def center_sign_in_button_click(self):
        time.sleep(5)
        self.element(Locators.CENTER_SING_IN_BUTTON).click()
        self.element(Locators.CENTER_SING_IN_BUTTON).click()
        time.sleep(1)

    def sign_in_with_mail(self, email, password):
        self.top_corner_sign_in_button_click()
        time.sleep(1)
        self.elements(Locators.SIGN_BUTTONS)[1].click()
        time.sleep(1)
        self.element(Locators.EMAIL_SWITCH).click()
        time.sleep(1)
        self.element(Locators.LOGIN_INPUT).send_keys(email)
        self.element(Locators.PASSWORD_INPUT).send_keys(password)
        self.element(Locators.CONTINUE_BUTTON).click()
        time.sleep(1)

    def sign_in_ktox(self):
        self.sign_in_with_mail('ktox', '123123123')

    def sign_up_with_mail(self, email, password, confirm_password):
        self.element(Locators.TOP_CORNER_SIGN_IN_BUTTON).click()
        time.sleep(1)
        self.elements(Locators.SIGN_BUTTONS)[0].click()
        time.sleep(1)
        self.element(Locators.EMAIL_SWITCH).click()
        time.sleep(1)
        self.element(Locators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.element(Locators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.element(Locators.REGISTER_PASSWORD_CONFIRM_INPUT).send_keys(confirm_password)
        time.sleep(2)
        self.element(Locators.CONTINUE_BUTTON).click()
        time.sleep(1)

    def sign_in_with_phone(self, phone):
        self.element(Locators.TOP_CORNER_SIGN_IN_BUTTON).click()
        self.elements(Locators.SIGN_BUTTONS)[1].click()
        self.element(Locators.PHONE_NUMBER_INPUT).send_keys(phone)
        time.sleep(1)
        self.element(Locators.CONTINUE_BUTTON).click()

    def sign_up_with_phone(self, phone):
        self.element(Locators.TOP_CORNER_SIGN_IN_BUTTON).click()
        time.sleep(1)
        self.elements(Locators.SIGN_BUTTONS)[0].click()
        time.sleep(1)
        self.element(
            Locators.PHONE_NUMBER_INPUT).click()  # какая то хрень с фокусом в поле телефона, нужно сперва кликуть
        self.element(Locators.PHONE_NUMBER_INPUT).send_keys(phone)
        time.sleep(1)
        self.element(Locators.CONTINUE_BUTTON).click()

    def error_message(self):
        return self.element(Locators.ERROR_MESSAGE).text

    def send_random_code(self):
        random_code = random.randint(1000, 9999)
        self.element(Locators.PHONE_CODE_INPUT).send_keys(random_code)
        time.sleep(2)
        self.submit()
        time.sleep(1)

    def submit(self):
        self.element(Locators.CONTINUE_BUTTON).click()

    def check_error_message_ru(self, error_ru):
        self.switch_lang_to_ru()
        print(f'\nТекущая ошибка: {self.error_message()} \nОжидаемая ошибка: {error_ru}')
        assert self.error_message() == error_ru, "неправильное сообщение об ошибке на русском"

    def check_error_message_en(self, error_en):
        self.switch_lang_to_en()
        print(f'\nТекущая ошибка: {self.error_message()} \nОжидаемая ошибка: {error_en}')
        assert self.error_message() == error_en, "неправильное сообщение об ошибке на английском"

    def check_error_message(self, error_ru, error_eng):  # какого хуя
        time.sleep(1)
        self.check_error_message_ru(error_ru)
        self.check_error_message_en(error_eng)
        self.switch_lang_to_ru()  # обратно на русский

    def reset_password_with_mail(self, mail):
        self.element(Locators.RESET_PASSWORD_BUTTON).click()
        time.sleep(1)
        self.element(Locators.EMAIL_SWITCH).click()
        time.sleep(1)
        self.element(Locators.RESET_EMAIL_INPUT).send_keys(mail + '\n')
        # self.element(Locators.RESET_PASSWORD_SEND_CODE_BUTTON).click() жду пока исправят задвоение блока
