import random
import time

from pages.auth_page import AuthPage
from pages.collection_page import CollectionPage
from pages.creation_page import CreationPage
from pages.main_page import MainPage
from pages.object_page import ObjectPage
from pages.profile_page import ProfilePage


class TestCreation:
    def test_create_place(self, driver):  # 380
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        creation_page = CreationPage(driver)
        random_number = random.randint(1, 10000)
        # creation_page.
        auth_page.sign_in_ktox()
        main_page.new_place()

        time.sleep(3)

    def test_create_link(self, driver):  # 381
        auth_page = AuthPage(driver)
        creation_page = CreationPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        object_page = ObjectPage(driver)

        auth_page.sign_in_ktox()
        main_page.new_link()
        random_number = random.randint(1, 10000)
        creation_page.create_link(f'ссылка {random_number}', f'{random_number}.com', 'описание')
        creation_page.select_category(random.randint(0, 13))
        creation_page.save_to_public()
        main_page.open_my_profile()
        profile_page.open_last_created_item()

        assert object_page.get_name() == f"ссылка {random_number}"
        assert object_page.get_type() == "ССЫЛКА"

    def test_create_note(self, driver):  # 382
        auth_page = AuthPage(driver)
        creation_page = CreationPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        object_page = ObjectPage(driver)

        auth_page.sign_in_ktox()
        main_page.new_note()
        random_number = random.randint(1, 10000)
        creation_page.create_note(f'заметка {random_number}', 'описание')
        creation_page.select_category(random.randint(0, 13))
        creation_page.save_to_public()
        main_page.open_my_profile()
        profile_page.open_last_created_item()

        assert object_page.get_name() == f"заметка {random_number}"
        assert object_page.get_type() == "ЗАМЕТКА"

    def test_create_collection(self, driver):  # 387
        auth_page = AuthPage(driver)
        creation_page = CreationPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        collection_page = CollectionPage(driver, None)

        auth_page.sign_in_ktox()
        main_page.new_collection()
        random_number = random.randint(1, 10000)
        creation_page.create_collection(f'подборка {random_number}', 'описание')
        creation_page.save_to_public()
        main_page.open_my_profile()
        profile_page.open_last_created_collection()

        assert collection_page.get_name() == f"подборка {random_number}"
