import time


from pages.auth_page import AuthPage
from pages.object_page import ObjectPage


class TestObject:
    def test_share_object(self, driver):
        auth_page = AuthPage(driver)
        object_page = ObjectPage(driver)
        auth_page.sign_in_ktox()
        object_page.open_note_object(97347)
        object_page.share()
        # не знаю как проверить буфер

    def test_like(self, driver):
        auth_page = AuthPage(driver)
        object_page = ObjectPage(driver)
        auth_page.sign_in_ktox()
        object_page.open_note_object(97347)
        object_page.check_like()
        time.sleep(4)

