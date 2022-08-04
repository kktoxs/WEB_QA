from selenium.webdriver.common.by import By


class ProfilePageLocators:
    LOGIN = (By.CSS_SELECTOR, 'h1[data-qa="profile-login"]')
    PRIVATE = (By.CSS_SELECTOR, 'div[data-qa="private-card"]')
    SHOW_COLLECTIONS = (By.CSS_SELECTOR, 'a[data-qa="show-all-collections"]')
    SHOW_OBJECTS = (By.CSS_SELECTOR, 'a[data-qa="show-all-objects"]')
    SHOW_ON_MAP = (By.CSS_SELECTOR, 'a[data-qa="show-map-button"]')
    