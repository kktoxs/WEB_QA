import time

from conftest import BASE_URL
from locators.creation_page_locators import CreationPageLocators as Locators
from pages.base_page import BasePage


class CreationPage(BasePage):
    url = BASE_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def create_place(self, title, description):
        self.element(Locators.CHOOSE_ADDRESS).click()
        self.element(Locators.TITLE).send_keys(title)

    def create_link(self, title, link, description):
        self.element(Locators.TITLE).send_keys(title)
        self.element(Locators.LINK).send_keys(link)
        self.element(Locators.DESCRIPTION).send_keys(description)

    def create_note(self, title, description):
        self.element(Locators.TITLE).send_keys(title)
        self.element(Locators.DESCRIPTION).send_keys(description)

    def create_collection(self, title, description):
        self.element(Locators.TITLE).send_keys(title)
        self.element(Locators.DESCRIPTION).send_keys(description)

    def save_to_public(self):
        self.element(Locators.CREATE_BUTTON).click()
        self.element(Locators.SAVE_TO_PUBLIC_BUTTON).click()
        time.sleep(1)

    def save_to_private(self):
        self.element(Locators.CREATE_BUTTON).click()
        self.element(Locators.SAVE_TO_PRIVATE_BUTTON).click()
        time.sleep(1)

    def save_to_collection(self):
        self.element(Locators.CREATE_BUTTON).click()
        self.element(Locators.SAVE_TO_COLLECTION_BUTTON).click()
        time.sleep(1)

    def select_category(self, num):
        self.element(Locators.ADD_CATEGORY).click()
        self.elements(Locators.CATEGORY)[num].click()
