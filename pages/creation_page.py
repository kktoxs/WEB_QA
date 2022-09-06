from locators.creation_page_locators import CreationPageLocators as Locators
from pages.base_page import BasePage


class CreationPage(BasePage):
    def link(self, title, link, description):
        self.element(Locators.TITLE).send_keys(title)
        self.element(Locators.LINK).send_keys(link)
        self.element(Locators.DESCRIPTION).send_keys(description)
