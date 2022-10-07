import time

from conftest import BASE_URL
from pages.base_page import BasePage

from locators.feed_page_locators import FeedPageLocators as Locators


class FeedPage(BasePage):
    url = BASE_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def like(self):
        self.element(Locators.LIKE).click()

    def get_like_counter(self):
        return self.element(Locators.LIKE).text

    def save_to_profile(self):
        self.element(Locators.SAVE).click()
        time.sleep(1)
