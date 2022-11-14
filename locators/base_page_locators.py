from selenium.webdriver.common.by import By


class BasePageLocators:
    # INACTIVE_LANGUAGE = (By.CLASS_NAME, 'footer__lang-button')
    LANGUAGE_ENG = (By.CSS_SELECTOR, 'button[value="en"]')
    LANGUAGE_RU = (By.CSS_SELECTOR, 'button[value="ru"]')

    MY_PROFILE = (By.CSS_SELECTOR, 'button[data-qa="navbar-log-out-button"]')

    BODY = (By.TAG_NAME, 'body')
