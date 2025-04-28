from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By 
import time
from .base_page import BasePage

class Page1(BasePage):
    SEARCH_FIELD = (By.ID, "cb1-edit")
    SEARCH_BTN = (By.CLASS_NAME, "nav-search-btn")

    def find(self, search):
        self.enter_text(self.SEARCH_FIELD, search)
        self.click(self.SEARCH_BTN)

    def isElementPresent(self):
            try:
                self.find_element(self.ERROR_MSG)
                return True
            except NoSuchElementException:
                return False 
