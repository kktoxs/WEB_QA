import time

from tests.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):
    def fill_fields_and_submit(self):
        name= 'Lasha'
        email= 'lasha@mail.ru'
        self.remove_footer()
        self.element_is_visible(Locators.CONTACT).click()
        self.element_is_visible(Locators.NAME).send_keys(name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.THEME).send_keys('Hello')
        self.element_is_visible(Locators.MESSAGE).send_keys('World')
        self.element_is_visible(Locators.BUTTOM).click()




