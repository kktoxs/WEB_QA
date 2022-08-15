from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.CSS_SELECTOR, 'svg[data-qa="navbar-logo-desktop"]')
    SEARCH = (By.CSS_SELECTOR, 'input[data-qa="navbar-search-input"]')

    #  FEED
    CREATE = (By.CSS_SELECTOR, 'svg[data-qa="select-creation-item"]')

    USER_MENU = (By.CSS_SELECTOR, 'div[data-qa="user-menu-button"]')
    PROFILE = (By.CSS_SELECTOR, 'a[data-qa="link-user"]')
    SETTINGS = (By.CSS_SELECTOR, 'svg[data-qa="navbar-settings-button"]')
    SIGN_OUT = (By.CSS_SELECTOR, 'div[data-qa="link-sign-out"]')
    CLOSE_USER_MENU = (By.CSS_SELECTOR, 'svg[data-qa="navbar-log-out-button"]')

    #  LANGUAGE = (By.CSS_SELECTOR, 'button[data-qa="lang-button"]')
    GOOGLE_PLAY = (By.CSS_SELECTOR, 'svg[data-qa="navbar-google-play-icon"]')

    COLLECTION = (By.CSS_SELECTOR, 'div[data-qa="preview-collections"]')
    OBJECT = (By.CSS_SELECTOR, 'a[data-qa="lite-item-card"]')
    COLLECTION_AUTHOR = (By.CSS_SELECTOR, 'a[data-qa="author-collection"]')
    COLLECTION_NAME = (By.CSS_SELECTOR, 'p[data-qa="collection-name"]')
