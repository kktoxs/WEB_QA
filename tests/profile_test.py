import time

from pages.profile_page import ProfilePage


class TestProfilePage:
    def test_show_on_map_counter_not_null(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.url = 'https://planetfor.me/user/22749'
        profile_page.open()
        show_on_map_text = profile_page.get_show_on_map_counter()
        assert show_on_map_text != '0 мест'
        time.sleep(5)


