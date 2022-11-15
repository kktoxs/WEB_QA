from selenium.webdriver.common.by import By


class ProfilePageLocators:
    LOGIN = (By.CSS_SELECTOR, 'h1[data-qa="profile-login"]')
    PRIVATE = (By.CSS_SELECTOR, 'div[data-qa="private-card"]')

    PUBLIC_PRIVATE = (By.CLASS_NAME, 'toggleSwitch-buttons')

    SHOW_COLLECTIONS = (By.CSS_SELECTOR, 'a[data-qa="show-all-collections"]')
    SHOW_OBJECTS = (By.CSS_SELECTOR, 'a[data-qa="show-all-objects"]')
    SHOW_ON_MAP = (By.CSS_SELECTOR, 'a[data-qa="show-map-button"]')
    SHOW_ON_MAP_COUNTER = (By.CLASS_NAME, 'map-button__counter')

    SUBSCRIBE = (By.CSS_SELECTOR, 'button[data-qa="subscribe-button"]')
    SUBSCRIBE_TEXT = (By.CSS_SELECTOR, 'p[class="fw-medium"]')

    SUBSCRIBERS_SUBSCRIPTIONS = (By.CLASS_NAME, 'fw-medium')

    OBJECTS = (By.CSS_SELECTOR, 'a[data-qa="lite-item-card"]')
    COLLECTIONS = (By.CSS_SELECTOR, 'a[data-qa="lite-collection-card"]')

    COLLECTIONS_IN_SHOW_ALL = (By.CSS_SELECTOR, 'a[data-qa="collection-card"]')
    OBJECTS_IN_SHOW_ALL = (By.CSS_SELECTOR, 'a[data-qa="lite-item-card"]')

    SHARE_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="share-button"]')
    CLICK_TO_COPY_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="copy-share-link-button"]')

    SUBSCRIPTION = (By.CSS_SELECTOR, 'a[data-qa="subscription-card"]')
    SUBSCRIBER = (By.CSS_SELECTOR, 'a[data-qa="subscriber-card"]')

    COLLECTIONS_OBJECTS_COUNT = (By.CLASS_NAME, 'itemsCount')
