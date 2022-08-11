from selenium.webdriver.common.by import By


class MapPageLocators:
    FILTER_BUTTON = (By.CSS_SELECTOR, 'svg[data-qa="map-filtration-btn"]')
    FILTRATION_CATEGORIES = (By.CSS_SELECTOR, 'div[data-qa="map-filtration-category-item"]')
