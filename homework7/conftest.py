import logging
import os
import allure
import pytest
from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        # default='chrome',
        default='remote',
        help='Enter browser name'
    )
    parser.addoption(
        '--url',
        default='http://192.168.0.190:8081/',
        help='Enter url'
    )
    parser.addoption(
        '--browser',
        default='chrome',
        choices=['chrome', 'firefox', 'opera'],
        help='Enter browser name for remote browser'
    )
    parser.addoption('--executor', default='192.168.0.190')
    parser.addoption('--version_browser', default='102.0')
    parser.addoption('--vns', default=False)


@allure.step('Start driver')
@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser_name = request.config.getoption('browser_name').lower()
    executor = request.config.getoption('executor')
    remote_browser = request.config.getoption('browser')
    version_browser = request.config.getoption('version_browser')
    vns = request.config.getoption('vns')

    log_path = os.path.dirname(__file__) + '\\logs'
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.DEBUG)
    ch = logging.FileHandler(os.path.join(log_path, f'{request.node.module.__name__}.log'))
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s| %(module)s |%(name)s | %(levelname)s | %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if browser_name == 'chrome':
        driver = webdriver.Chrome(options=options)
        logger.info(f'Start driver {browser_name}')
        driver.implicitly_wait(5)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
        logger.info(f'Start driver {browser_name}')
        driver.implicitly_wait(5)
    elif browser_name == 'opera':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', True)
        driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)
        logger.info(f'Start driver {browser_name}')
        driver.implicitly_wait(5)
    elif browser_name == 'remote':
        capabilities = {
            "browserName": remote_browser,
            "browserVersion": version_browser,
            "selenoid:options": {
                "enableVNC": vns,
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub',
            desired_capabilities=capabilities)
        logger.info(f'Start driver remote with {remote_browser} browser')
    else:
        logger.error('Driver not started. Wrong browser name')
        raise AssertionError('Driver not started. Wrong browser name. Choose browser: chrome, firefox, opera or remote')
    driver.logger = logger
    yield driver
    logger.info(f'Stop driver {browser_name} \n'+'='*110)
    driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')
