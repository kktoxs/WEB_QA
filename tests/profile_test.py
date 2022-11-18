import time
import pyperclip as buffer
from selenium.common import TimeoutException

from conftest import DENCHIG_ID, KTOX_ID
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfilePage:
    def test_show_on_map_counter(self, driver):
        profile_page = ProfilePage(driver)
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)

        profile_page.open_profile(KTOX_ID)
        # до авторизации
        show_on_map_text = profile_page.get_show_on_map_counter()
        assert show_on_map_text != '0 мест'
        # после авторизации
        auth_page.sign_in_ktox()
        main_page.open_my_profile()
        show_on_map_text_authorized = profile_page.get_show_on_map_counter()
        assert show_on_map_text_authorized != '0 мест'
        assert show_on_map_text == show_on_map_text_authorized

    def test_show_on_map_personal_counter(self, driver):
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        auth_page.sign_in_ktox()
        main_page.open_my_profile()
        profile_page.switch_to_personal()
        # до обновления страницы
        show_on_map_text = profile_page.get_show_on_map_counter()
        assert show_on_map_text != '0 мест'
        # после обновления страницы
        driver.refresh()
        show_on_map_text_refreshed = profile_page.get_show_on_map_counter()
        assert show_on_map_text_refreshed != '0 мест'
        # сравнить
        assert show_on_map_text == show_on_map_text_refreshed

    def test_subscribe(self, driver):  # 3100
        auth_page = AuthPage(driver)
        profile_page = ProfilePage(driver)
        auth_page.sign_in_ktox()
        my_subscriptions_before = profile_page.get_my_subscriptions_count()
        profile_page.open_random_profile_unsubscribed()
        subscribers_before = profile_page.get_subscribers_count()
        profile_page.subscribe()
        subscribers_after = profile_page.get_subscribers_count()
        assert subscribers_before == subscribers_after - 1, \
            "При подписке на пользователя его кол-во подписчиков не увелививается"
        my_subscriptions_after = profile_page.get_my_subscriptions_count()
        assert my_subscriptions_before == my_subscriptions_after - 1, \
            "При подписке кол-во моих подписок не увеличилось"

    def test_unsubscribe(self, driver):
        auth_page = AuthPage(driver)
        profile_page = ProfilePage(driver)
        auth_page.sign_in_ktox()
        my_subscriptions_before = profile_page.get_my_subscriptions_count()
        profile_page.open_random_profile_subscribed()
        subscribers_before = profile_page.get_subscribers_count()
        profile_page.unsubscribe()
        profile_page.refresh()  # баг с отпиской #751
        subscribers_after = profile_page.get_subscribers_count()
        assert subscribers_before == subscribers_after + 1, \
            "При отписке от пользователя его кол-во подписчиков не уменьшается"
        my_subscriptions_after = profile_page.get_my_subscriptions_count()
        assert my_subscriptions_before == my_subscriptions_after + 1, \
            "При отписке кол-во моих подписок не уменьшилось"

    # def test_subscribe_all(self, driver):
    #     auth_page = AuthPage(driver)
    #     profile_page = ProfilePage(driver)
    #     auth_page.sign_in_ktox()
    #     for i in range(10000):
    #         profile_page.open_profile(i)
    #         try:
    #             profile_page.subscribe()
    #         except TimeoutException:
    #             print(i)

    def test_share_profile(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.open_profile(DENCHIG_ID)
        profile_page.share_profile()
        copied_url = buffer.paste()
        driver.get(copied_url)
        assert profile_page.get_login() == 'denchig', 'ссылка с профиля denchig ведет не туда'
        profile_page.open_profile(KTOX_ID)
        profile_page.share_profile()
        copied_url = buffer.paste()
        driver.get(copied_url)
        assert profile_page.get_login() == 'ktox_ui', 'ссылка с профиля ktox ведет не туда'

    def test_subscriptions_count(self, driver):  # 328
        profile_page = ProfilePage(driver)
        profile_page.open_profile(KTOX_ID)
        subscriptions_count_in_profile = profile_page.get_subscriptions_count()
        subscriptions_count_in_subscriptions = profile_page.count_subscriptions()
        assert subscriptions_count_in_subscriptions == subscriptions_count_in_profile
        profile_page.open_profile(DENCHIG_ID)
        subscriptions_count_in_profile = profile_page.get_subscriptions_count()
        subscriptions_count_in_subscriptions = profile_page.count_subscriptions()
        assert subscriptions_count_in_subscriptions == subscriptions_count_in_profile

    def test_subscribers_count(self, driver):  # 327
        profile_page = ProfilePage(driver)
        profile_page.open_profile(KTOX_ID)
        subscribers_count_in_profile = profile_page.get_subscribers_count()
        subscribers_count_in_subscribers = profile_page.count_subscribers()
        assert subscribers_count_in_profile == subscribers_count_in_subscribers
        profile_page.open_profile(DENCHIG_ID)
        subscribers_count_in_profile = profile_page.get_subscribers_count()
        subscribers_count_in_subscribers = profile_page.count_subscribers()
        assert subscribers_count_in_profile == subscribers_count_in_subscribers

    def test_collections_in_profile(self, driver):  # 330
        profile_page = ProfilePage(driver)

        profile_page.open_profile(KTOX_ID)
        collections_fits_in_profile = profile_page.get_collections_count() <= 6
        assert collections_fits_in_profile != profile_page.check_if_show_collections_button_is_visible()

        profile_page.open_profile(DENCHIG_ID)
        collections_fits_in_profile = profile_page.get_collections_count() <= 6
        assert collections_fits_in_profile != profile_page.check_if_show_collections_button_is_visible()

    def test_objects_in_profile(self, driver):  # 329
        profile_page = ProfilePage(driver)

        profile_page.open_profile(KTOX_ID)
        objects_fits_in_profile = profile_page.get_objects_count() <= 24
        assert objects_fits_in_profile != profile_page.check_if_show_objects_button_is_visible()

        profile_page.open_profile(DENCHIG_ID)
        objects_fits_in_profile = profile_page.get_objects_count() <= 24
        assert objects_fits_in_profile != profile_page.check_if_show_objects_button_is_visible()

    def test_collections_in_personal(self, driver):  # 336 и 334
        auth_page = AuthPage(driver)
        profile_page = ProfilePage(driver)
        auth_page.sign_in_ktox()
        profile_page.open_my_profile()
        profile_page.switch_to_personal()

        collections_fits_in_profile = profile_page.get_collections_count() <= 6
        assert collections_fits_in_profile != profile_page.check_if_show_collections_button_is_visible()

        objects_fits_in_profile = profile_page.get_objects_count() <= 24
        assert objects_fits_in_profile != profile_page.check_if_show_objects_button_is_visible()

    def test_show_collections_in_profile(self, driver):  # 337
        profile_page = ProfilePage(driver)

        profile_page.open_profile(DENCHIG_ID)
        count_in_profile = profile_page.get_collections_count()
        assert count_in_profile == profile_page.count_collections()

    def test_show_objects_in_profile(self, driver):  # 331
        profile_page = ProfilePage(driver)

        profile_page.open_profile(DENCHIG_ID)
        count_in_profile = profile_page.get_objects_count()
        assert count_in_profile == profile_page.count_objects()
