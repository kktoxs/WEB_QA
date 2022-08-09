from selenium.webdriver.common.by import By


class SettingsPageLocators:
    PROFILE_SETTINGS = (By.CSS_SELECTOR, 'button[data-qa="settings-edit-profile-button"]')
    LOGIN_INPUT = (By.CSS_SELECTOR, 'input[data-qa="login-input"]')
    NAME_INPUT = (By.CSS_SELECTOR, 'input[data-qa="name-input"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[data-qa="reset-password-email-input"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[data-qa="city-input"]')
    DESCRIPTION = (By.CSS_SELECTOR, 'div[data-qa="about-me"]')

    CHANGE_PASSWORD = (By.CSS_SELECTOR, 'button[data-qa="settings-change-password-button"]')
    OLD_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-qa="old-password-input"]')
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'div[data-qa="show-password-button"]')
    NEW_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-qa="new-password-input"]')
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-qa="confirm-password-input"]')
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'div[data-qa="reset-password-link"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="auth-button"]')

    BLOCKED_ACCOUNTS = (By.CSS_SELECTOR, 'button[data-qa="settings-blocked-accounts-button"]')
    # BLOCKED_ACCOUNTS_LIST

    LANGUAGE_BUTTON_RU = (By.CSS_SELECTOR, 'button[data-qa="settings-language-button-ru"]')
    LANGUAGE_BUTTON_EN = (By.CSS_SELECTOR, 'button[data-qa="settings-language-button-en"]')

    TG_BOT_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="settings-tb-bot-button"]')
    # GENERATE_KEY_BUTTON
    # COPY_KEY_BUTTON
    # GENERATE_NEW_KEY_BUTTON
    # KEY_TEXT
