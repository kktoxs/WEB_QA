from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.CSS_SELECTOR, 'svg[data-qa="navbar-logo-desktop"]')
    SEARCH = (By.CSS_SELECTOR, 'input[data-qa="navbar-search-input"]')
    #  FEED
    CREATE = (By.CSS_SELECTOR, 'svg[data-qa="select-creation-item"]')
    PROFILE = (By.CSS_SELECTOR, 'div[data-qa="user-menu-button"]')
    GOOGLE_PLAY = (By.CSS_SELECTOR, 'svg[data-qa="navbar-google-play-icon"]')
    COLLECTION = (By.CSS_SELECTOR, 'div[data-qa="preview-collections"]')
    OBJECT = (By.CSS_SELECTOR, 'a[data-qa="lite-item-card"]')
    #  LANGUAGE = (By.CSS_SELECTOR, 'button[data-qa="lang-button"]')
    COLLECTION_AUTHOR = (By.CSS_SELECTOR, 'a[data-qa="author-collection"]')
    COLLECTION_NAME = (By.CSS_SELECTOR, 'p[data-qa="collection-name"]')