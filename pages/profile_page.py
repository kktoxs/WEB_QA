from selenium.common import TimeoutException

from conftest import BASE_URL
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators as Locators


class ProfilePage(BasePage):
    url = BASE_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)

    # def get_profile_url(self):
    # TODO()

    def open_profile(self, num):
        self.open_url(BASE_URL + '/user/' + str(num))

    def get_login(self):
        return self.element(Locators.LOGIN).text

    def show_private(self):
        self.elements(Locators.PUBLIC_PRIVATE)[1].click()

    def show_public(self):
        self.elements(Locators.PUBLIC_PRIVATE)[0].click()

    def show_on_map(self):
        self.element(Locators.SHOW_ON_MAP).click()

    def get_show_on_map_counter(self):
        return self.element(Locators.SHOW_ON_MAP_COUNTER).text

    def subscribe(self):
        if self.elements(Locators.SUBSCRIBE_TEXT)[1].text == "Подписаться":
            print(f"\nПодписываюсь на {self.get_login()}")
            self.element(Locators.SUBSCRIBE).click()
        else:
            print("Нет кнопки Подписаться")

    def unsubscribe(self):
        if self.elements(Locators.SUBSCRIBE_TEXT)[1].text == "Отписаться":
            print(f"\nОтписываюсь от {self.get_login()}")
            self.element(Locators.SUBSCRIBE).click()
        else:
            print("Нет кнопки Отписаться")

    def get_subscriptions_count(self):
        count = int(self.elements(Locators.SUBSCRIBERS_SUBSCRIPTIONS)[1].text)
        print(f"\n{self.get_login()}: {count} подписок")
        return count

    def get_subscribers_count(self):
        count = int(self.elements(Locators.SUBSCRIBERS_SUBSCRIPTIONS)[0].text)
        print(f"\n{self.get_login()}: {count} Подписчиков")
        return count

    def get_my_subscriptions_count(self):
        self.open_my_profile()
        return self.get_subscriptions_count()

    def get_my_subscribers_count(self):
        self.open_my_profile()
        return self.get_subscribers_count()
