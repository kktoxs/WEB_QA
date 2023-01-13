import random
import time

import allure

from pages.auth_page import AuthPage
from pages.collection_page import CollectionPage
from pages.creation_page import CreationPage
from pages.main_page import MainPage
from pages.object_page import ObjectPage
from pages.profile_page import ProfilePage


class TestCreation:

    @allure.feature('Создание')
    @allure.story('Создание в профиль')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное создание места')
    @allure.link('https://kiwi.pfm.team/case/380/')
    def test_create_place(self, driver):  # 380
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        creation_page = CreationPage(driver)
        object_page = ObjectPage(driver)

        auth_page.sign_in_ktox()
        main_page.new_place()
        random_number = random.randint(1, 10000)
        creation_page.create_place(f'место {random_number}', 'описание')
        creation_page.select_category(random.randint(0, 13))
        creation_page.save_to_public()
        main_page.open_my_profile()
        profile_page.open_last_created_item()

        assert object_page.get_name() == f"место {random_number}"
        assert object_page.get_type() == "МЕСТО"

    @allure.feature('Создание')
    @allure.story('Создание в профиль')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное создание ссылки')
    @allure.link('https://kiwi.pfm.team/case/381/')
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

    @allure.feature('Создание')
    @allure.story('Создание в профиль')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное создание заметки')
    @allure.link('https://kiwi.pfm.team/case/382/')
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

    @allure.feature('Создание')
    @allure.story('Создание в профиль')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное создание коллекции')
    @allure.link('https://kiwi.pfm.team/case/387/')
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

    @allure.feature('Создание')
    @allure.story('Создание в личное')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное создание места')
    @allure.link('https://kiwi.pfm.team/case/380/')
    def test_create_place_in_personal(self, driver):  # 380
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        creation_page = CreationPage(driver)
        object_page = ObjectPage(driver)

        auth_page.sign_in_ktox()
        main_page.new_place()
        random_number = random.randint(1, 10000)
        creation_page.create_place(f'место {random_number}', 'описание')
        creation_page.select_category(random.randint(0, 13))
        creation_page.save_to_private()
        main_page.open_my_profile()
        profile_page.switch_to_personal()
        profile_page.open_last_created_item()

        assert object_page.get_name() == f"место {random_number}"
        assert object_page.get_type() == "МЕСТО"

    @allure.feature('Создание')
    @allure.story('Создание в личное')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное создание ссылки')
    @allure.link('https://kiwi.pfm.team/case/381/')
    def test_create_link_in_personal(self, driver):  # 381
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
        creation_page.save_to_private()
        main_page.open_my_profile()
        profile_page.switch_to_personal()
        profile_page.open_last_created_item()

        assert object_page.get_name() == f"ссылка {random_number}"
        assert object_page.get_type() == "ССЫЛКА"

    @allure.feature('Создание')
    @allure.story('Создание в личное')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное создание заметки')
    @allure.link('https://kiwi.pfm.team/case/382/')
    def test_create_note_in_personal(self, driver):  # 382
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
        creation_page.save_to_private()
        main_page.open_my_profile()
        profile_page.switch_to_personal()
        profile_page.open_last_created_item()

        assert object_page.get_name() == f"заметка {random_number}"
        assert object_page.get_type() == "ЗАМЕТКА"

    @allure.feature('Создание')
    @allure.story('Создание в личное')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное создание коллекции')
    @allure.link('https://kiwi.pfm.team/case/387/')
    def test_create_collection_in_personal(self, driver):  # 387
        auth_page = AuthPage(driver)
        creation_page = CreationPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        collection_page = CollectionPage(driver, None)

        auth_page.sign_in_ktox()
        main_page.new_collection()
        random_number = random.randint(1, 10000)
        creation_page.create_collection(f'подборка {random_number}', 'описание')
        creation_page.save_to_private()
        main_page.open_my_profile()
        profile_page.switch_to_personal()
        profile_page.open_last_created_collection()

        assert collection_page.get_name() == f"подборка {random_number}"

    # @allure.feature('Создание')
    # @allure.story('Создание в коллекцию')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('Успешное создание ссылки')
    # @allure.link('https://kiwi.pfm.team/case/381/')

    # @allure.feature('Создание')
    # @allure.story('Создание в коллекцию')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('Успешное создание заметки')
    # @allure.link('https://kiwi.pfm.team/case/382/')

    # @allure.feature('Создание')
    # @allure.story('Создание в коллекцию')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title('Успешное создание коллекции')
    # @allure.link('https://kiwi.pfm.team/case/387/')