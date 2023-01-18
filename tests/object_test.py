import time

import allure
import pyperclip as buffer

from conftest import KTOX_ID, DENCHIG_ID
from pages.auth_page import AuthPage
from pages.object_page import ObjectPage
from pages.profile_page import ProfilePage


class TestObject:
    def test_share_object(self, driver):  # 341
        profile_page = ProfilePage(driver)
        object_page = ObjectPage(driver)

        profile_page.open_profile(DENCHIG_ID)
        profile_page.open_random_object()
        name = object_page.get_name()
        object_page.share()
        copied_url = buffer.paste()
        driver.get(copied_url)
        assert object_page.get_name() == name

        profile_page.open_profile(KTOX_ID)
        profile_page.open_random_object()
        name = object_page.get_name()
        object_page.share()
        copied_url = buffer.paste()
        driver.get(copied_url)
        assert object_page.get_name() == name

        profile_page.open_random_profile_with_objects()
        profile_page.open_random_object()
        name = object_page.get_name()
        object_page.share()
        copied_url = buffer.paste()
        driver.get(copied_url)
        assert object_page.get_name() == name

    @allure.feature('Сущность')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Правильное имя автора сущности')
    @allure.link('https://kiwi.pfm.team/case/352/')
    def test_author(self, driver):  # 352
        profile_page = ProfilePage(driver)
        object_page = ObjectPage(driver)
        profile_page.open_random_profile_with_objects()
        profile_page.open_random_object()
        author = object_page.get_author()
        object_page.open_author()
        assert author == profile_page.get_login(), "Не совпадает логин автора в профиле и в сущности"
