from conftest import BASE_URL
from pages.base_page import BasePage
from locators.settings_page_locators import SettingsPageLocators as Locators


class SettingsPage(BasePage):
    url = BASE_URL + '/settings/profile-edit'

    def __init__(self, driver):
        super(SettingsPage, self).__init__(driver, self.url)

    def change_name(self, new_name):
        self.element(Locators.NAME_INPUT).clear()
        self.element(Locators.NAME_INPUT).send_keys(new_name)
        self.element(Locators.CHANGE_BUTTON).click()

    def change_city(self, new_city):
        self.element(Locators.CITY_INPUT).clear()
        self.element(Locators.CITY_INPUT).send_keys(new_city)
        self.element(Locators.CHANGE_BUTTON).click()

    def change_description(self, description):
        self.element(Locators.DESCRIPTION).clear()
        self.element(Locators.DESCRIPTION).send_keys(description)
        self.element(Locators.CHANGE_BUTTON).click()

