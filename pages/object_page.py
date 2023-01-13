import random
import time
import pyperclip

from conftest import BASE_URL
from pages.base_page import BasePage
from locators.object_page_locators import ObjectPageLocators as Locators


class ObjectPage(BasePage):
    url = BASE_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def open_place_object(self, num):
        self.driver.get(BASE_URL + '/place/' + str(num))

    def open_link_object(self, num):
        self.driver.get(BASE_URL + '/link/' + str(num))

    def open_note_object(self, num):
        self.driver.get(BASE_URL + '/note/' + str(num))

    def check_like(self):
        before = int(self.get_likes_counter())
        print(f"До лайка: {before}")
        self.like()
        after = int(self.get_likes_counter())
        print(f"После лайка: {after}")
        assert before == after - 1
        self.like()  # возвращаю как было

    def like(self):
        self.element(Locators.LIKES).click()

    def get_likes_counter(self):
        return self.element(Locators.LIKES).text

    def save(self):
        self.element(Locators.SAVES).click()

    def get_author(self):
        author = self.element(Locators.AUTHOR_NAME).text
        print(f"Автор сущности \"{self.get_name()}\" - {author}")
        return author

    def show_on_map(self):
        self.element(Locators.SHOW_ON_MAP).click()

    def open_link(self):
        self.element(Locators.OPEN_LINK).click()

    def share(self):
        self.element(Locators.SHARE_BUTTON).click()
        time.sleep(0.5)
        self.element(Locators.COPY_SHARE_LINK).click()

    def open_link_from_clipboard(self, link):
        self.driver.get(link)

    def get_info(self):
        return self.element(Locators.INFO).text  # data qa

    def get_name(self):
        name = self.element(Locators.NAME).text
        print(f"\nимя сущности: {name}")
        return name

    def get_category(self):
        return self.elements(Locators.TYPE_AND_CATEGORY)[1].text

    def get_type(self):
        return self.elements(Locators.TYPE_AND_CATEGORY)[0].text

    def open_author(self):
        print(f"Открывается профиль автора сущности \"{self.get_name()}\"")
        self.element(Locators.AUTHOR).click()
