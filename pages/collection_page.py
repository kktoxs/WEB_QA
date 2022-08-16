from conftest import BASE_URL
from pages.base_page import BasePage
from locators.collection_page_locators import CollectionPageLocators as Locators


class CollectionPage(BasePage):
    url = BASE_URL + '/collection/'

    def __init__(self, driver, collection_num):
        collection_url = self.url + str(collection_num)
        super().__init__(driver, collection_url)
        super(CollectionPage, self).open()

    def like(self):
        self.element(Locators.LIKES).click()

    def get_like_color(self):
        color = self.element(Locators.LIKES).value_of_css_property('Color')
        if color == 'rgb(152, 160, 173)':
            return 'GREY'
        if color == 'rgb(255, 49, 71)':
            return 'RED'
        if color == 'rgb(152, 160, 173)':
            return 'GREY'


    def save(self):
        self.element(Locators.SAVES).click()

    def get_show_on_map_counter(self):
        return self.element(Locators.SHOW_ON_MAP_COUNTER).text
