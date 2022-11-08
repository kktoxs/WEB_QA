from selenium.webdriver.common.by import By


class ObjectPageLocators:
    NAME = (By.CSS_SELECTOR, 'h1[data-qa="item-name"]')
    AUTHOR = (By.CSS_SELECTOR, 'a[data-qa="author-view"]')
    AUTHOR_NAME = (By.CSS_SELECTOR, 'p[class="ml-8 f-lineClamp-vertical-1"]')

    IMAGE = (By.CLASS_NAME, 'image__wrapper')
    IMAGE_COUNTER = (By.CSS_SELECTOR, 'span[data-qa="item-cover-counter"]')

    CLOSE_IMAGE_BUTTON = (By.CSS_SELECTOR, 'svg[data-qa="gallery-close-btn"]')
    PREV_IMAGE_BUTTON = (By.CSS_SELECTOR, 'svg[data-qa="nav-btn-left"]')
    NEXT_IMAGE_BUTTON = (By.CSS_SELECTOR, 'svg[data-qa="nav-btn-right"]')

    SHARE_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="action-button-share"]')
    COPY_SHARE_LINK = (By.CSS_SELECTOR, 'button[data-qa="copy-share-link-button"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="action-button-save"]')

    TYPE = (By.CSS_SELECTOR, 'p[data-qa="type-chip"]')
    CATEGORY = (By.CSS_SELECTOR, 'p[data-qa="category-chip"]')
    TYPE_AND_CATEGORY = (By.CLASS_NAME, "chip__category")

    INFO_BUTTON = (By.CLASS_NAME, 'info-icon-wrap')
    INFO = (By.CLASS_NAME, 'entity-info-date')
    LIKES = (By.CSS_SELECTOR, 'span[data-qa="like-counter"]')
    SAVES = (By.CSS_SELECTOR, 'span[data-qa="save-counter"]')
    CONTEXT_MENU = (By.CLASS_NAME, 'class="ctx-icon"')

    # и развернуть, и свернуть
    COLLAPSE_TEXT_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="collapsed-text-button"]')

    # для места
    SHOW_ON_MAP = (By.CSS_SELECTOR, 'a[data-qa="map-button"]')
    ADDRESS = (By.CSS_SELECTOR, 'p[data-qa="address-string-url"]')

    # для ссылки
    OPEN_LINK = (By.CSS_SELECTOR, 'a[data-qa="link-button"]')
    LINK = (By.CSS_SELECTOR, 'p[data-qa="address-string-url"]')

    INCLUDED_IN_COLLECTION = (By.CLASS_NAME, 'content__secondary-card-children')

    #  YANDEX_TAXI
    #  GOOGLE_MAPS
    #  YANDEX_MAPS
