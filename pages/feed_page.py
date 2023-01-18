import time

from selenium.webdriver import Keys

from conftest import BASE_URL
from pages.base_page import BasePage

from locators.feed_page_locators import FeedPageLocators as Locators


class FeedPage(BasePage):
    url = BASE_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def like(self, i):  # сломалось
        self.elements(Locators.LIKE)[i].click()

    def get_like_counter(self, i):
        return self.elements(Locators.LIKE)[i].text

    def save_to_profile(self, i):
        self.elements(Locators.SAVE)[i].click()
        time.sleep(1)

    def get_author_name(self, i):
        string = self.elements(Locators.PUBLISH_TEXT)[i].text
        login = string.split(' ', 1)[0]
        return login

    def get_description(self):
        return self.element(Locators.DESCRIPTION).text

    def get_date(self):
        return self.element(Locators.ITEM_DATE).text

    def category(self):
        return self.element(Locators.ITEM_CATEGORY).text

    def open_item(self, i):
        self.elements(Locators.ITEM_NAME)[i].click()

    def item_name(self):
        return self.element(Locators.ITEM_NAME).text

    def open_collection(self):
        categories = self.elements(Locators.ITEM_CATEGORY)
        for i in range(len(categories)):
            if categories[i].text == "ПОДБОРКА":
                self.elements(Locators.ITEM_NAME)[i].click()
                break
        print("Нет подборок в ленте")

    def get_publication_category(self, text):
        if 'место' in text:
            return 'место'
        elif 'ссылк' in text:
            return 'ссылка'
        elif 'заметк' in text:
            return 'заметка'
        elif 'подборк' in text:
            return 'коллекция'

    def like_collection_and_check(self):
        categories = self.elements(Locators.ITEM_CATEGORY)
        for i in range(len(categories)):
            if categories[i].text == "ПОДБОРКА":
                before = self.get_like_counter(i)
                self.like(i)
                after = self.get_like_counter(i)
                print(f"\nПодборка: было {before}, стало {after}")
                assert before != after, "сломался лайк в ленте у подборки"
                return
        print("Нет подборок в ленте")

    def like_item_and_check(self):
        feed_items = self.elements(Locators.PUBLISH_TEXT)
        for i in range(len(feed_items)):
            if self.get_publication_category(feed_items[i].text) != 'коллекция':
                before = self.get_like_counter(i)
                self.like(i)
                after = self.get_like_counter(i)
                print(f"\nСущность: было {before}, стало {after}")
                assert before != after, "сломался лайк в ленте у сущности"
                return
        print("Нет сущностей в ленте")

    def reset_filters(self):
        self.element(Locators.FILTER_BUTTON).click()
        time.sleep(1)
        self.elements(Locators.TYPE)[0].click()
        self.elements(Locators.CATEGORY)[0].click()
        self.element(Locators.FILTER_BUTTON).click()
        time.sleep(1)

    def get_all_publications(self):
        return self.elements(Locators.ITEM_NAME)

    def compare_posts(self, first, second):
        first.click()
        prev_url = self.driver.tabs_handles[1]
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)
        second.click()
        time.sleep(3)
        next_url = self.driver.current_url
        assert prev_url != next_url, f"Дубли в ленте: {next_url}"

    def check_only_collection_in_feed(self):
        publishes = self.elements(Locators.PUBLISH_TEXT)
        categories = self.elements(Locators.ITEM_CATEGORY)
        for i in range(len(publishes)):
            if ("подбор" not in publishes[i].text) or (categories[i].text != "ПОДБОРКА"):
                assert False, f"\nВ ленте пост, не соответствующий фильтру \"подборки\": {publishes[i].text} \n" \
                              f"Категория - {categories[i].text} "

    def check_only_places_in_feed(self):
        publishes = self.elements(Locators.PUBLISH_TEXT)
        for i in range(len(publishes)):
            if "место" not in publishes[i].text:
                assert False, f"\nВ ленте пост, не соответствующий фильтру \"места\": {publishes[i].text}"

    def check_only_notes_in_feed(self):
        publishes = self.elements(Locators.PUBLISH_TEXT)
        for i in range(len(publishes)):
            if "заметк" not in publishes[i].text:
                assert False, f"\nВ ленте пост, не соответствующий фильтру \"заметки\": {publishes[i].text}"

    def check_only_links_in_feed(self):
        publishes = self.elements(Locators.PUBLISH_TEXT)
        for i in range(len(publishes)):
            if "ссылк" not in publishes[i].text:
                assert False, f"\nВ ленте пост, не соответствующий фильтру \"ссылки\": {publishes[i].text}"

    def check_only_category_in_feed(self, category):
        categories = self.elements(Locators.ITEM_CATEGORY)
        for i in range(len(categories)):
            if categories[i].text != category.upper():
                assert False, f"\nВ ленте пост, не соответствующий фильтру \"{category}\"\n" \
                              f"Категория - {categories[i].text}"

    def switch_to_subscriptions(self):
        self.elements(Locators.SUBSCRIPTIONS_WORLD)[0].click()

    def switch_to_world(self):
        self.elements(Locators.SUBSCRIPTIONS_WORLD)[1].click()

    def check_only_diff_in_feed(self):
        self.check_only_category_in_feed('разное')

    def check_only_info_in_feed(self):
        self.check_only_category_in_feed('инфо')

    def check_only_food_in_feed(self):
        self.check_only_category_in_feed('еда')

    def check_only_bars_in_feed(self):
        self.check_only_category_in_feed('бары')

    def check_only_leisure_in_feed(self):
        self.check_only_category_in_feed('досуг')

    def check_only_shops_in_feed(self):
        self.check_only_category_in_feed('покупки')

    def check_only_look_in_feed(self):
        self.check_only_category_in_feed('посмотреть')

    def check_only_housing_in_feed(self):
        self.check_only_category_in_feed('жильё')

    def check_only_sport_in_feed(self):
        self.check_only_category_in_feed('спорт')

    def check_only_tasks_in_feed(self):
        self.check_only_category_in_feed('дела')

    def check_only_transport_in_feed(self):
        self.check_only_category_in_feed('транспорт')

    def check_only_education_in_feed(self):
        self.check_only_category_in_feed('образование')

    def check_only_medicine_in_feed(self):
        self.check_only_category_in_feed('медицина')

    def check_only_beauty_in_feed(self):
        self.check_only_category_in_feed('красота')

    def filter_by_type(self, num):
        self.element(Locators.FILTER_BUTTON).click()
        time.sleep(1)
        self.elements(Locators.TYPE)[num].click()
        self.element(Locators.FILTER_BUTTON).click()
        time.sleep(1)

    def filter_by_category(self, num):
        self.element(Locators.FILTER_BUTTON).click()
        time.sleep(1)
        self.elements(Locators.CATEGORY)[num].click()
        self.element(Locators.FILTER_BUTTON).click()
        time.sleep(1)

    def filter_all_type(self):
        self.filter_by_type(0)

    def filter_places(self):
        self.filter_by_type(1)

    def filter_links(self):
        self.filter_by_type(2)

    def filter_notes(self):
        self.filter_by_type(3)

    def filter_items(self):
        self.filter_by_type(1)
        self.filter_by_type(2)
        self.filter_by_type(3)

    def filter_collections(self):
        self.filter_by_type(4)

    def filter_all_category(self):
        self.filter_by_category(0)

    def filter_diff(self):
        self.filter_by_category(1)

    def filter_info(self):
        self.filter_by_category(2)

    def filter_food(self):
        self.filter_by_category(3)

    def filter_bars(self):
        self.filter_by_category(4)

    def filter_leisure(self):
        self.filter_by_category(5)

    def filter_shops(self):
        self.filter_by_category(6)

    def filter_to_look(self):
        self.filter_by_category(7)

    def filter_housing(self):
        self.filter_by_category(8)

    def filter_sport(self):
        self.filter_by_category(9)

    def filter_tasks(self):
        self.filter_by_category(10)

    def filter_transport(self):
        self.filter_by_category(11)

    def filter_education(self):
        self.filter_by_category(12)

    def filter_medicine(self):
        self.filter_by_category(13)

    def filter_beauty(self):
        self.filter_by_category(14)

    def set_filter_category_and_check(self, num):
        self.element(Locators.FILTER_BUTTON).click()
        time.sleep(1)
        self.elements(Locators.CATEGORY)[num].click()
        category = self.elements(Locators.CATEGORY)[num].text
        self.element(Locators.FILTER_BUTTON).click()
        time.sleep(1)
        self.check_only_category_in_feed(category)
        self.reset_filters()
