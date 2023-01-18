import time
from random import randint

import allure

from pages.auth_page import AuthPage
from pages.collection_page import CollectionPage
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.object_page import ObjectPage


class TestFeed:
    @allure.feature('Лента новостей')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Лайк сущности')
    @allure.link('https://kiwi.pfm.team/case/371/')
    def test_like_object(self, driver):  # 371
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        auth_page.sign_in_ktox()
        main_page.open_feed()

        feed_page.like_item_and_check()  # сломан лайк

    @allure.feature('Лента новостей')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Лайк сущности')
    @allure.link('https://kiwi.pfm.team/case/371/')
    def test_like_collection(self, driver):  # 371
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        auth_page.sign_in_ktox()
        main_page.open_feed()

        feed_page.like_collection_and_check()

    @allure.feature('Лента новостей')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Фильтр типов')
    @allure.link('https://kiwi.pfm.team/case/370/')
    def test_filter_types(self, driver):  # 370
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        auth_page.sign_in_ktox()
        main_page.open_feed()

        feed_page.filter_collections()
        feed_page.check_only_collection_in_feed()
        feed_page.reset_filters()

        feed_page.filter_notes()
        feed_page.check_only_notes_in_feed()
        feed_page.reset_filters()

        feed_page.filter_places()
        feed_page.check_only_places_in_feed()
        feed_page.reset_filters()

        feed_page.filter_links()
        feed_page.check_only_links_in_feed()
        feed_page.reset_filters()

    @allure.feature('Лента новостей')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Фильтр категорий')
    @allure.link('https://kiwi.pfm.team/case/370/')
    def test_filter_categories(self, driver):  # 370
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        auth_page.sign_in_ktox()
        main_page.open_feed()
        for i in range(1, 15):
            feed_page.set_filter_category_and_check(i)

    def test_author_item(self, driver):  # 375
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        object_page = ObjectPage(driver)

        auth_page.sign_in_ktox()
        main_page.open_feed()
        feed_page.filter_items()
        num = randint(0, 10)
        author_in_feed = feed_page.get_author_name(num)
        feed_page.open_item(num)
        author_in_item = object_page.get_author()  # жду пока смогу вытащить ник

        assert author_in_item == author_in_feed, 'Неправильный автор сущности'

    def test_author_collection(self, driver):  # 375
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        collection_page = CollectionPage(driver, 0)

        auth_page.sign_in_ktox()
        main_page.open_feed()
        feed_page.filter_collections()
        num = randint(0, 10)
        author_in_feed = feed_page.get_author_name(num)
        feed_page.open_item(num)
        author_in_item = collection_page.get_author()  # жду пока смогу вытащить ник
        assert author_in_item == author_in_feed, 'Неправильный автор подборки'

    def test_read_more(self, driver):  # 373
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        object_page = ObjectPage(driver)
        collection_page = CollectionPage(driver, 0)
        auth_page.sign_in_ktox()
        main_page.open_feed()
        feed_page.filter_items()  # жду локатор Читать полностью

