"""
This test covers DuckDuckGo searches
"""
import pytest
import logging
import logging.config

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from tests.web.test_base import BaseTest


@pytest.mark.web
class TestSearch(BaseTest):

    LOGGER = logging.getLogger(__name__)

    @pytest.mark.parametrize('phrase', ['panda', 'covid', 'python', 'pytest'])
    def test_basic_duckduckgo_search(self, phrase):

        self.LOGGER.info("Inside Test")
        search_page = DuckDuckGoSearchPage(self.driver)
        result_page = DuckDuckGoResultPage(self.driver)
        # phrase = "panda"

        # Given the DuckDuckGo home page is displayed
        search_page.load()

        # assert if the page loaded successfully
        assert search_page.is_loaded() is True

        # When the user searches the title
        search_page.search(phrase)

        # And the search result query is "phrase"
        assert phrase in result_page.search_input_value()

        # And the search result links pertain to "phrase"
        titles = result_page.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        print(matches)
        assert len(matches) > 0

        # Then the search result title contains "phrase"
        assert phrase in result_page.title()
        self.LOGGER.info("Finishing Test")
