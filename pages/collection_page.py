from pages.base_page import BasePage
from locators.collection_page_locators import CollectionPageLocators as Locators


class CollectionPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        super(CollectionPage, self).open()

    def like(self):
        self.element(Locators.LIKES).click()

    def save(self):
        self.element(Locators.SAVES).click()

    def get_show_on_map_counter(self):
        return self.element(Locators.SHOW_ON_MAP_COUNTER).text
