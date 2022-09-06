import time

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfilePage:
    def test_show_on_map_counter(self, driver):
        profile_page = ProfilePage(driver)
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)

        profile_page.url = 'https://planetfor.me/user/23475'
        profile_page.open()
        # до авторизации
        show_on_map_text = profile_page.get_show_on_map_counter()
        assert show_on_map_text != '0 мест'
        auth_page.sign_in_with_mail('ktox', '123123123')
        # auth_page.submit()
        main_page.open_my_profile()
        # после авторизации
        show_on_map_text_authorized = profile_page.get_show_on_map_counter()
        assert show_on_map_text_authorized != '0 мест'
        assert show_on_map_text == show_on_map_text_authorized

    def test_show_on_map_personal_counter(self, driver):
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        auth_page.sign_in_with_mail('ktox', '123123123')
        # auth_page.submit()
        main_page.open_my_profile()
        profile_page.show_private()
        # до обновления страницы
        show_on_map_text = profile_page.get_show_on_map_counter()
        assert show_on_map_text != '0 мест'
        # после обновления страницы
        driver.refresh()
        show_on_map_text_refreshed = profile_page.get_show_on_map_counter()
        assert show_on_map_text_refreshed != '0 мест'
        # сравнить
        assert show_on_map_text == show_on_map_text_refreshed

    # def test_subscription(self, driver):
