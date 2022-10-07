from selenium.webdriver.common.by import By


class FeedPageLocators:
    LIKE = (By.CSS_SELECTOR, 'span[data-qa="like-counter"]')
    SAVE = (By.CSS_SELECTOR, 'span[data-qa="save-counter"]')
    
