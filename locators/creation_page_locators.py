from selenium.webdriver.common.by import By


class CreationPageLocators:
    CREATE_BUTTON = (By.CSS_SELECTOR, 'h6[data-qa="creation-next-step-btn"]')
    TITLE = (By.CSS_SELECTOR, 'textarea[data-qa="creation-title-area"]')
    LINK = (By.CSS_SELECTOR, 'textarea[data-qa="creation-link-area"]')
    DESCRIPTION = (By.CSS_SELECTOR, 'textarea[data-qa="creation-description-area"]')
    ADD_CATEGORY = (By.CLASS_NAME, "selected-categories-btn")
    CATEGORY = (By.CSS_SELECTOR, 'div[data-qa="creation-categories"]')
