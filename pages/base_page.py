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

    def open_my_profile(self):
        self.element(Locators.MY_PROFILE).click()

    def element(self, locator, timeout=2):
        try:
            return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"\nЭлемент {locator} не найден")

    def elements(self, locator, timeout=2):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")

    def switch_lang_to_en(self):
        self.element(Locators.LANGUAGE_ENG).click()

    def switch_lang_to_ru(self):
        self.element(Locators.LANGUAGE_RU).click()

    def close_tab(self):
        self.driver.close()
