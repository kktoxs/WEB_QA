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
