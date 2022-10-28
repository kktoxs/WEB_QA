import time
from random import randint

from pages.auth_page import AuthPage
from pages.collection_page import CollectionPage
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.object_page import ObjectPage


class TestFeed:
    def test_like(self, driver):  # 371
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        auth_page.sign_in_ktox()
        main_page.open_feed()

        feed_page.like_item_and_check()
        feed_page.like_collection_and_check()

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

    def test_read_more(self, driver):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        object_page = ObjectPage(driver)
        collection_page = CollectionPage(driver, 0)
        auth_page.sign_in_ktox()
        main_page.open_feed()
        feed_page.filter_items()  # жду локатор Читать полностью

    def test_switch_to_world(self, driver):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        auth_page.sign_in_ktox()
        main_page.open_feed()
        feed_page.switch_to_world()
        time.sleep(10)  # мира не будет

    def test_duplicates(self, driver):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        auth_page.sign_in_ktox()
        main_page.open_feed()
        publications = feed_page.get_all_publications()

        for i in range(len(publications)-1):
            previous_post = publications[i]
            next_post = publications[i+1]
            if previous_post.text == next_post.text:
                feed_page.compare_posts(previous_post, next_post)  # разобраться с переключением вкладок


