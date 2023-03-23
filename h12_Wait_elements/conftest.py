import pytest
from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        default='chrome',
        choices=['chrome', 'firefox', 'opera'],
        help='Enter name of browser'
    )
    parser.addoption(
        '--url',
        default='http://localhost/',
        help='Enter url'
    )


@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser_name = request.config.getoption('browser_name').lower()
    if browser_name == 'chrome':
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    elif browser_name == 'opera':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', True)
        driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)
        driver.implicitly_wait(5)
    else:
        raise Exception('Choose browser: chrome, firefox or opera')
    yield driver
    driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')
