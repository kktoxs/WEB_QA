import time

from pages.auth_page import AuthPage
from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestFeed:
    def test_like(self, driver):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        auth_page.sign_in_ktox()
        main_page.open_feed()
        feed_page.filter_places()
        feed_page.check_only_places_in_feed()
        time.sleep(10)

    def test_filter_types(self, driver):
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

    def test_filter_categories(self, driver):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        auth_page.sign_in_ktox()
        main_page.open_feed()
        for i in range(1, 15):
            feed_page.set_filter_category_and_check(i)
