import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators as Locators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def open_url(self, url):
        self.driver.get(url)

    def is_logged_in(self):  # Проверяет видимость кнопки создания (она есть только у авторизованных)
        try:
            Wait(self.driver, 3).until(EC.visibility_of_element_located(Locators.ADD_ITEM))
        except TimeoutException:
            return False
        return True

    def open_my_profile(self):
        self.element(Locators.MY_PROFILE).click()

    def element(self, locator, timeout=5):
        try:
            return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:  # добавить скриншоты
            print(f"Элемент {locator} не найден")

    def elements(self, locator, timeout=5):
        try:
            return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            print(f"Элементы {locator} не найден")

    def scroll_down(self):
        self.element(
            Locators.LANGUAGE_RU).click()
        # приходится тыкать на кнопку рус чтобы прокрутить страницу вниз, скрипт скролла не работает

    def check_if_scrolled_down(self):
        if self.elements(Locators.LANGUAGE_BUTTONS)[0].is_displayed():
            print('visible')
            return True
        else:
            print('invisible')
            return False

    def switch_lang_to_en(self):
        self.elements(Locators.LANGUAGE_RU)[1].click()  #  пока не поправили data qa

    def switch_lang_to_ru(self):
        self.elements(Locators.LANGUAGE_RU)[0].click()

    def close_tab(self):
        self.driver.close()

    def paste_in_new_tab(self):
        self.driver.get('https://google.com')
        self.element(Locators.GOOGLE_SEARCH).send_keys(Keys.CONTROL + "v\n")

    def refresh(self):
        self.driver.refresh()


