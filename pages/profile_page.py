from conftest import BASE_URL
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators as Locators


class ProfilePage(BasePage):
    url = BASE_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)

    # def get_profile_url(self):
    # TODO()

    def get_login(self):
        return self.element(Locators.LOGIN).text

    def show_private(self):
        self.element(Locators.PRIVATE).click()

    def show_on_map(self):
        self.element(Locators.SHOW_ON_MAP).click()

    def get_show_on_map_counter(self):
        return self.element(Locators.SHOW_ON_MAP_COUNTER).text

    def open_personal(self):
        self.element(Locators.PRIVATE).click()
