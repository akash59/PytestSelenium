import json

import pytest
import selenium.webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='session')
def config():
    # Read the file

    with open('./config//config.json', mode='r') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Edge']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # return config object
    return config


@pytest.fixture()
def driver(config):
    # initialize the chromedriver instance
    if config['browser'] == 'Firefox':
        browser = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())

    elif config['browser'] == 'Chrome':
        browser = selenium.webdriver.Chrome(executable_path=ChromeDriverManager().install())

    elif config['browser'] == 'Edge':
        browser = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())

    elif config['browser'] == 'Headless Chrome':
        chrome_options = selenium.webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        browser = selenium.webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # add the implicit wait
    browser.implicitly_wait(int(config['implicit_wait']))

    # maximize the browser window
    browser.maximize_window()

    # return the web driver instance for the setup
    yield browser

    # quit the driver for the cleanup
    if browser is not None:
        browser.quit()