import time

from conftest import BASE_URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):
    url = BASE_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def open_my_profile(self):
        self.element(Locators.USER_MENU).click()

    def search(self, text):
        self.element(Locators.SEARCH).send_keys(text + '\n')

    def new_place(self):
        self.element(Locators.CREATE).click()
        self.elements(Locators.CREATION_ITEM)[0].click()

    def new_link(self):
        self.element(Locators.CREATE).click()
        self.elements(Locators.CREATION_ITEM)[1].click()

    def new_note(self):
        self.element(Locators.CREATE).click()
        self.elements(Locators.CREATION_ITEM)[2].click()

    def new_collection(self):
        self.element(Locators.CREATE).click()
        self.elements(Locators.CREATION_ITEM)[3].click()

    def open_feed(self):
        self.element(Locators.FEED).click()
        time.sleep(2)

