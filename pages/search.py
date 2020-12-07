from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.basepage import BasePage


class DuckDuckGoSearchPage(BasePage):

    # Locators
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    URL = "https://duckduckgo.com"

    # Initializers
    def __init__(self, browser):
        super().__init__(browser)

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def is_loaded(self):
        search_input = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        return search_input.is_displayed()

    def search(self, keyword):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(keyword + Keys.RETURN)