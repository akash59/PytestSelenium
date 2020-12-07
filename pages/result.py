from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.basepage import BasePage


class DuckDuckGoResultPage(BasePage):
    # Locators
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # Initializers
    def __init__(self, browser):
        super().__init__(browser)

    def is_loaded(self):
        result_links = self.wait.until(EC.presence_of_element_located(self.RESULT_LINKS))
        return len(result_links) > 5

    # Interaction Methods
    def result_link_titles(self):
        result_links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in result_links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return str(search_input.get_attribute('value')).strip()

    def title(self):
        return self.browser.title
