from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):
    url = 'https://planetfor.me/'

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def open_my_profile(self):
        self.element(Locators.USER_MENU).click()

    def search(self, text):
        self.element(Locators.SEARCH).send_keys(text + '\n')

    def open_profile(self, login):
        self.search(login)
        self.element()
