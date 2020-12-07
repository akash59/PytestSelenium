import json
import os

import pytest
import selenium.webdriver


@pytest.fixture(scope='session')
def config():
    # Read the file

    with open('./config//config.json', mode='r') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # return config object
    return config


@pytest.fixture()
def browser(config):
    # initialize the chromedriver instance
    if config['browser'] == 'Firefox':
        ff_options = selenium.webdriver.FirefoxOptions()
        ff_options.binary_location = os.environ['FIREFOX_EXECUTABLE_PATH']
        browser = selenium.webdriver.Firefox(options=ff_options, executable_path=os.environ['FIREFOX_BINARY_PATH'])

    elif config['browser'] == 'Chrome':
        chrome_options = selenium.webdriver.ChromeOptions()
        browser = selenium.webdriver.Chrome(options=chrome_options, executable_path=os.environ['CHROME_BINARY_PATH'])

    elif config['browser'] == 'Headless Chrome':
        chrome_options = selenium.webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        browser = selenium.webdriver.Chrome(options=chrome_options, executable_path=os.environ['CHROME_BINARY_PATH'])
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
