import time

from pages.search_page import SearchPage


class TestSearchPage:
    def test_search(self, driver):
        search_page = SearchPage(driver)
        search_page.search('qa')
        search_page.scroll_down()  # не работает
        search_page.filter_places()
        search_page.filter_profiles()
        time.sleep(5)
