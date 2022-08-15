from selenium.webdriver.common.by import By


class SearchPageLocators:
    LOADING = (By.CLASS_NAME, 'lds-ring')
    RESULTS = (By.CLASS_NAME, 'search-page__main-section')
    PROFILE_LOGIN = (By.CSS_SELECTOR, 'p[data-qa="search-profile-login"]')
    COLLECTION = (By.CLASS_NAME, 'collection')
    ITEM_NAME = (By.CSS_SELECTOR, 'p[data-qa="search-item-name"]')
    ITEM_AUTHOR = (By.CSS_SELECTOR, 'p[data-qa="search-item-login"]')
    NO_RESULTS = (By.CLASS_NAME, 'no-results')

    FILTER = (By.CLASS_NAME, 'filtration-group-name')
    CATEGORY = (By.CLASS_NAME, 'filtration-category-name')
