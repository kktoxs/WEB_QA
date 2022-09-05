from pages.base_page import BasePage
from locators.object_page_locators import ObjectPageLocators as Locators


class ObjectPage(BasePage):
    def like(self):
        self.element(Locators.LIKES).click()

    def save(self):
        self.element(Locators.SAVES).click()

    def get_author(self):
        return self.element(Locators.AUTHOR_NAME).text
