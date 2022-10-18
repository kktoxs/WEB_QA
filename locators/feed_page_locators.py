from selenium.webdriver.common.by import By


class FeedPageLocators:
    LIKE = (By.CSS_SELECTOR, 'span[data-qa="like-counter"]')
    SAVE = (By.CSS_SELECTOR, 'span[data-qa="save-counter"]')

    SAVE_TO_PUBLIC = (By.CSS_SELECTOR, 'div[data-qa="save-to-public-btn"]')
    SAVE_TO_PROFILE = (By.CSS_SELECTOR, 'div[data-qa="save-to-private-btn"]')
    SAVE_TO_COLLECTION = (By.CSS_SELECTOR, 'div[data-qa="save-to-collection-btn"]')

    PUBLISH_TEXT = (By.CLASS_NAME, 'published-text')
    DESCRIPTION = (By.CLASS_NAME, 'description')

    ITEM_DATE = (By.CLASS_NAME, 'date')
    ITEM_CATEGORY = (By.CLASS_NAME, 'feed-image-category')
    ITEM_NAME = (By.CLASS_NAME, 'item-name')

    FILTER_BUTTON = (By.CLASS_NAME, 'feed-filtration-icon')
    TYPE = (By.CLASS_NAME, 'filtration-group-name')
    CATEGORY = (By.CLASS_NAME, 'filtration-category-name')
