from pages.base_page import BasePage
from locators.search_page_locators import SearchPageLocators as Locators


class SearchPage(BasePage):
    url = 'https://planetfor.me'

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver, self.url)

    def search(self, text):
        self.url = f'https://planetfor.me/search?inquiry={text}'
        super(SearchPage, self).open()

    def filter_places(self):
        self.elements(Locators.FILTER)[1].click()

    def filter_links(self):
        self.elements(Locators.FILTER)[2].click()

    def filter_notes(self):
        self.elements(Locators.FILTER)[3].click()

    def filter_collections(self):
        self.elements(Locators.FILTER)[4].click()

    def filter_profiles(self):
        self.elements(Locators.FILTER)[5].click()

    def category_diff(self):
        self.element(Locators.CATEGORY)[1].click()

    def category_info(self):
        self.element(Locators.CATEGORY)[2].click()

    def category_food(self):
        self.element(Locators.CATEGORY)[3].click()

    def category_bars(self):
        self.element(Locators.CATEGORY)[4].click()

    def category_leisure(self):
        self.element(Locators.CATEGORY)[5].click()

    def category_shops(self):
        self.element(Locators.CATEGORY)[6].click()

    def category_to_look(self):
        self.element(Locators.CATEGORY)[7].click()

    def category_housing(self):
        self.element(Locators.CATEGORY)[8].click()

    def category_sport(self):
        self.element(Locators.CATEGORY)[9].click()

    def category_tasks(self):
        self.element(Locators.CATEGORY)[10].click()

    def category_transport(self):
        self.element(Locators.CATEGORY)[11].click()

    def category_education(self):
        self.element(Locators.CATEGORY)[12].click()

    def category_medicine(self):
        self.element(Locators.CATEGORY)[13].click()

    def category_beauty(self):
        self.element(Locators.CATEGORY)[14].click()
