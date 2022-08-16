import time

from pages.auth_page import AuthPage
from pages.collection_page import CollectionPage


class TestCollectionPage:
    def test_show_on_map_counter(self, driver):
        auth_page = AuthPage(driver)
        collection_page = CollectionPage(driver, 100953)

        auth_page.sign_in_with_mail('ktox', '123123123')
        time.sleep(1)
        show_on_map_counter = collection_page.get_show_on_map_counter()
        assert show_on_map_counter != '0 мест'
        driver.refresh()
        show_on_map_counter_refreshed = collection_page.get_show_on_map_counter()
        assert show_on_map_counter_refreshed != '0 мест'

    def test_collection_like(self, driver):

        auth_page = AuthPage(driver)
        collection_page = CollectionPage(driver, 100953)
        assert collection_page.get_like_color() == 'GREY', 'красный лайк у неавторизованного'
        # захожу в профиль
        auth_page.sign_in_with_mail('ktox', '123123123')
        time.sleep(1)
        assert collection_page.get_like_color() == 'RED', 'лайкнутая коллекция не красная'
        collection_page.like()  # убираю лайк
        assert collection_page.get_like_color() == 'GREY', 'коллекция без лайка красная'

        collection_page.like()  # возвращаю лайк обратно для следующих тестов


