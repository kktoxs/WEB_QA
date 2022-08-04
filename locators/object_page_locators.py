from selenium.webdriver.common.by import By


class ObjectPageLocators:
    SHARE_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="action-button-share"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="action-button-save"]')
    OBJECT_TYPE = (By.CSS_SELECTOR, 'p[data-qa="type-chip"]')
    CATEGORY = (By.CSS_SELECTOR, 'p[data-qa="category-chip"]')
    #  INFO
    #  LIKES
    #  SAVES
    AUTHOR = (By.CSS_SELECTOR, 'a[data-qa="author-view"]')
    COLLAPSE_TEXT_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="collapsed-text-button"]')
    SHOW_ON_MAP = (By.CSS_SELECTOR, 'a[data-qa="map-button"]')
    ADDRESS = (By.CSS_SELECTOR, 'p[data-qa="address-string-url"]')
    #  YANDEX_TAXI
    #  GOOGLE_MAPS
    #  YANDEX_MAPS
