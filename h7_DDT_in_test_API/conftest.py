import requests
import pytest


@pytest.fixture
def request_resource():
    return requests


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        action='store',
        default='https://ya.ru/',
        help='Enter URL'
    )
    parser.addoption(
        '--code',
        default=200,
        help='Status code'
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def request_status_code(request):
    # return getattr(request.config.getoption('--status_code'))
    return request.config.getoption('--code')
