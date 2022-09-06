import time

from pages.auth_page import AuthPage
from pages.main_page import MainPage


class TestCreation:
    def test_create_place(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', '123123123')
        main_page = MainPage(driver)
        main_page.create_place()
        time.sleep(3)

    def test_create_link(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', '123123123')
        main_page = MainPage(driver)
        main_page.create_link()
        time.sleep(3)

    def test_create_note(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', '123123123')
        main_page = MainPage(driver)
        main_page.create_note()
        time.sleep(3)

    def test_create_collection(self, driver):
        auth_page = AuthPage(driver)
        auth_page.sign_in_with_mail('ktox', '123123123')
        main_page = MainPage(driver)
        main_page.create_collection()
        time.sleep(3)

