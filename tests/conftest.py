import json
import smtplib
import pytest
import selenium.webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import shutil
import tempfile


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Headless Chrome")
    parser.addoption("--explicit_wait", action="store", default=20)


@pytest.fixture(scope="session")
def get_param(request):
    config_param = {
        "browser": request.config.getoption("--browser"),
        "explicit_wait": int(request.config.getoption("--explicit_wait"))
    }
    return config_param


@pytest.fixture(scope='session')
def config(get_param):
    # Read the file
    with open('./config//config.json', mode='r') as config_file:
        config = json.load(config_file)

    for key in get_param.keys():
        if key in config.keys():
            config[key] = get_param[key]

    with open("./config//config.json", "w") as config_file:
        json.dump(config, config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Edge']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # return config object
    return config


@pytest.fixture(scope="class")
def driver(config, request):
    # logger.info("Running setup method for the Test Case .......")
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

    request.cls.driver = browser

    # add the implicit wait
    browser.implicitly_wait(int(config['implicit_wait']))

    # maximize the browser window
    browser.maximize_window()

    # return the web driver instance for the setup
    yield browser

    # logger.info("Running teardown method for the Test Case .......")
    # quit the driver for the cleanup
    if browser is not None:
        browser.quit()


@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print("finalizing {} ({})".format(smtp_connection, server))
    smtp_connection.close()


@pytest.fixture
def cleandir():
    old_cwd = os.getcwd()
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    yield
    os.chdir(old_cwd)
    shutil.rmtree(newpath)
