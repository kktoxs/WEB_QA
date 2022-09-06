import random
import time

from pages.auth_page import AuthPage
from pages.creation_page import CreationPage
from pages.main_page import MainPage


class TestCreation:
    def test_create_place(self, driver):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        creation_page = CreationPage(driver)

        auth_page.sign_in_with_mail('ktox', '123123123')
        main_page.new_place()

        time.sleep(3)

    def test_create_link(self, driver):
        auth_page = AuthPage(driver)
        creation_page = CreationPage(driver)
        main_page = MainPage(driver)

        auth_page.sign_in_with_mail('ktox', '123123123')
        # for i in range(1,1000):
        main_page.new_link()
        random_number = random.randint(1, 100)
        creation_page.create_link(f'автотестовая ссылка {random_number}', f'{random_number}.com', 'описание')
        creation_page.select_category(random.randint(0, 13))
        creation_page.save_to_public()

    def test_create_note(self, driver):
        auth_page = AuthPage(driver)
        creation_page = CreationPage(driver)
        main_page = MainPage(driver)

        auth_page.sign_in_with_mail('ktoxtest', '123123123')
        for i in range(1, 500):
            main_page.new_note()
            random_number = random.randint(1, 100)
            creation_page.create_note(f'автотестовая заметка {random_number}', 'описание')
            creation_page.select_category(random.randint(0, 13))
            creation_page.save_to_public()
        time.sleep(3)

    def test_create_collection(self, driver):
        auth_page = AuthPage(driver)
        creation_page = CreationPage(driver)
        main_page = MainPage(driver)

        auth_page.sign_in_with_mail('ktox', '123123123')
        main_page.new_collection()
        time.sleep(3)
