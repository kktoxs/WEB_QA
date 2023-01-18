import random
import time

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

    def switch_to_personal(self):
        self.elements(Locators.PUBLIC_PRIVATE)[1].click()
        time.sleep(1)

    def switch_to_public(self):
        self.elements(Locators.PUBLIC_PRIVATE)[0].click()
        time.sleep(1)

    def show_on_map(self):
        self.element(Locators.SHOW_ON_MAP).click()

    def get_show_on_map_counter(self):
        return self.element(Locators.SHOW_ON_MAP_COUNTER).text

    def subscribe(self):
        if self.elements(Locators.SUBSCRIBE_TEXT)[1].text == "Подписаться":
            print(f"Подписываюсь на {self.get_login()}")
            self.element(Locators.SUBSCRIBE).click()
            time.sleep(0.5)
        else:
            print("Нет кнопки Подписаться|Уже подписан")

    def unsubscribe(self):
        if self.elements(Locators.SUBSCRIBE_TEXT)[1].text == "Отписаться":
            print(f"Отписываюсь от {self.get_login()}")
            self.element(Locators.SUBSCRIBE).click()
            time.sleep(0.5)
        else:
            print("Нет кнопки Отписаться|Уже отписан")

    def get_subscriptions_count(self):
        count = int(self.elements(Locators.SUBSCRIBERS_SUBSCRIPTIONS)[1].text)
        print(f"\n{self.get_login()}: {count} Подписок в профиле")
        return count

    def get_subscribers_count(self):
        count = int(self.elements(Locators.SUBSCRIBERS_SUBSCRIPTIONS)[0].text)
        print(f"\n{self.get_login()}: {count} Подписчиков в профиле")
        return count

    def get_my_subscriptions_count(self):
        self.open_my_profile()
        time.sleep(1)
        return self.get_subscriptions_count()

    def get_my_subscribers_count(self):
        self.open_my_profile()
        return self.get_subscribers_count()

    def open_last_created_item(self):
        self.elements(Locators.OBJECTS)[0].click()
        time.sleep(1)

    def open_last_created_collection(self):
        self.elements(Locators.COLLECTIONS)[0].click()
        time.sleep(1)

    def share_profile(self):
        self.element(Locators.SHARE_BUTTON).click()
        time.sleep(0.5)
        self.element(Locators.CLICK_TO_COPY_BUTTON).click()

    def count_subscriptions(self):
        self.elements(Locators.SUBSCRIBERS_SUBSCRIPTIONS)[1].click()
        time.sleep(1)
        for i in range(50):
            self.scroll_down()
            time.sleep(0.05)
        try:
            count = len(self.elements(Locators.SUBSCRIPTION))
        except TimeoutException:
            count = 0
        print(f"{self.get_login()}: {count} Подписок внутри блока подписки")
        return count

    def count_subscribers(self):
        self.elements(Locators.SUBSCRIBERS_SUBSCRIPTIONS)[0].click()
        time.sleep(1)
        for i in range(50):
            self.scroll_down()
            time.sleep(0.05)

        try:
            count = len(self.elements(Locators.SUBSCRIBER))
        except TimeoutException:
            count = 0
        print(f"{self.get_login()}: {count} Подписчиков внутри блока подписчики")
        return count

    def open_subscribers(self):
        self.elements(Locators.SUBSCRIBERS_SUBSCRIPTIONS)[0].click()

    def open_subscriptions(self):
        self.elements(Locators.SUBSCRIBERS_SUBSCRIPTIONS)[1].click()

    def check_if_show_collections_button_is_visible(self):
        show = self.element(Locators.SHOW_COLLECTIONS)
        if show is not None:
            print(f"{self.get_login()}: Есть кнопка показать все коллекции")
            return True
        else:
            print(f"{self.get_login()}: Нет кнопки показать все коллекции")
            return False

    def check_if_show_objects_button_is_visible(self):
        show = self.element(Locators.SHOW_OBJECTS)
        if show is not None:
            print(f"{self.get_login()}: Есть кнопка показать все сущности")
            return True
        else:
            print(f"{self.get_login()}: Нет кнопки показать все сущности")
            return False

    def get_collections_count(
            self):  # пока нет data qa у счетчиков, то при отсутсвии коллекций здесь будет счетчик сущностей
        count = int(self.elements(Locators.COLLECTIONS_OBJECTS_COUNT)[0].text)
        print(f"\n{self.get_login()}: {count} коллекций")
        return count

    def get_objects_count(self):
        try:
            count = int(self.elements(Locators.COLLECTIONS_OBJECTS_COUNT)[1].text)
            print(f"{self.get_login()}: {count} сущностей")
            return count
        except IndexError:
            print("Нет сущностей")
            return 0

    def count_collections(self):
        self.show_all_collections()
        self.scroll_down()
        count = len(self.elements(Locators.COLLECTIONS_IN_SHOW_ALL))
        print(f"{self.get_login()}: {count} коллекций в блоке \"Показать все\"")
        return count

    def count_objects(self):
        self.show_all_objects()
        self.scroll_down()
        count = len(self.elements(Locators.OBJECTS_IN_SHOW_ALL))
        print(f"{self.get_login()}: {count} сущностей в блоке \"Показать все\"")
        return count

    def check_if_subscribe_button_available(self):
        subscribe = self.element(Locators.SUBSCRIBE)
        if subscribe is not None:
            if subscribe.text == "Подписаться":
                return True
            else:
                return False
        else:
            return False

    def open_random_profile_unsubscribed(self):
        random_id = random.randint(1, 25000)
        continue_searching = True
        while continue_searching:
            self.open_profile(random_id)
            continue_searching = not self.check_if_subscribe_button_available()
            random_id = random.randint(1, 25000)
        time.sleep(1)

    def open_random_profile_subscribed(self):
        self.open_my_profile()
        self.open_subscriptions()
        count = self.count_subscriptions()
        self.elements(Locators.SUBSCRIPTION)[random.randint(0, count - 1)].click()
        time.sleep(1)

    def show_all_objects(self):
        self.element(Locators.SHOW_OBJECTS).click()
        time.sleep(1)

    def show_all_collections(self):
        self.element(Locators.SHOW_COLLECTIONS).click()
        time.sleep(1)

    def open_random_object(self):
        if self.check_if_show_objects_button_is_visible():
            count = self.count_objects() - 1
            i = random.randint(0, count)
            self.elements(Locators.OBJECTS_IN_SHOW_ALL)[i].click()
        else:
            i = random.randint(0, len(self.elements(Locators.OBJECTS)) - 1)
            self.elements(Locators.OBJECTS)[i].click()

    def check_if_have_objects(self):
        objects = self.elements(Locators.OBJECTS)
        if objects is None:
            return False
        else:
            return True

    def open_random_profile_with_objects(self):
        random_id = random.randint(1, 25000)
        continue_searching = True
        while continue_searching:
            self.open_profile(random_id)
            continue_searching = not self.check_if_have_objects()
            random_id = random.randint(1, 25000)
