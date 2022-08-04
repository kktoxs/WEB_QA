from selenium.webdriver.common.by import By


class AuthPageLocators:
    TOP_CORNER_SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'svg[data-qa="user-menu-log-out-button"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="auth-button"]')
    # SIGN_UP_BUTTON = TODO
    EMAIL_SWITCH = (By.CSS_SELECTOR, 'span[data-qa="switch-button-singUp"]')
    MOBILE_SWITCH = (By.CSS_SELECTOR, 'span[data-qa="switch-button--enter"]')
    LOGIN_INPUT = (By.CSS_SELECTOR, 'input[data-qa="signIn-login-input"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-qa="auth-password-input"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="sign-in-button"]')
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'div[data-qa="show-password-button"]')
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'span[data-qa="reset-password-button"]')
    RESET_PASSWORD_SEND_CODE_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="reset-password-button"]')
    RESET_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[data-qa="reset-password-email-input"]')
    GOOGLE_BUTTON = (By.CLASS_NAME, 'google-btn')
    VK_BUTTON = (By.CLASS_NAME, 'vk-btn')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'span[data-qa="auth-credentials-error"]')

