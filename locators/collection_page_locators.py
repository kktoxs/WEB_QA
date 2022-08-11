from selenium.webdriver.common.by import By


class CollectionPageLocators:
    NAME = (By.CSS_SELECTOR, 'h1[data-qa="item-name"]')
    AUTHOR = (By.CSS_SELECTOR, 'a[data-qa="author-view"]')
    DESCRIPTION = (By.CSS_SELECTOR, 'p[data-qa="collapsed-text"]')
    COLLAPSE_TEXT_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="collapsed-text-button"]')
    SHOW_ON_MAP_BUTTON = (By.CSS_SELECTOR, 'a[data-qa="map-button"]')
    SHOW_ON_MAP_COUNTER = (By.CLASS_NAME, 'map-button__counter')
    ITEMS_COUNTER = (By.CLASS_NAME, 'itemsCount')
    LIKES = (By.CSS_SELECTOR, 'span[data-qa="like-counter"]')
    SAVES = (By.CSS_SELECTOR, 'span[data-qa="save-counter"]')


