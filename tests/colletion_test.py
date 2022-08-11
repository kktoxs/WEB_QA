import time

from pages.auth_page import AuthPage
from pages.collection_page import CollectionPage


class TestCollectionPage:
    def test_show_on_map_counter(self, driver):
        auth_page = AuthPage(driver)
        collection_page = CollectionPage(driver, 'https://planetfor.me/collection/100953')

        auth_page.sign_in_with_mail('ktox', '123123123')

        show_on_map_counter = collection_page.get_show_on_map_counter()
        assert show_on_map_counter != '0 мест'
        driver.refresh()
        show_on_map_counter_refreshed = collection_page.get_show_on_map_counter()
        assert show_on_map_counter_refreshed != '0 мест'
