from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 20)

    def is_loaded(self):
        pass
