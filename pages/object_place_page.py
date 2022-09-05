from conftest import BASE_URL
from pages.base_page import BasePage
from locators.object_page_locators import ObjectPageLocators as Locators
from pages.object_page import ObjectPage


class ObjectPlacePage(BasePage, ObjectPage):
    url = BASE_URL + '/place/'

    def __init__(self, driver, place_num):
        place_url = self.url + str(place_num)
        super().__init__(driver, place_url)
        super(ObjectPlacePage, self).open()

    def show_on_map(self):
        self.element(Locators.SHOW_ON_MAP).click()

    def open_link(self):
        self.element(Locators.OPEN_LINK).click()


