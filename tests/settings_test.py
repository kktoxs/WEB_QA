import time

from pages.auth_page import AuthPage
from pages.settings_page import SettingsPage


class TestSettingsPage:

    def test_change_name(self, driver):
        settings_page = SettingsPage(driver)
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', '123123123')
        settings_page.open_my_profile()
        time.sleep(10)

