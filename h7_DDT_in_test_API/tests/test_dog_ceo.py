import pytest
from jsonschema import validate
from h7_DDT_in_test_API.data.tests_data import *


@pytest.mark.validation
@pytest.mark.parametrize('link', ['s/list/all', 's/image/random', '/hound/images', '/hound/list'])
def test_validation_list_all_breads(request_resource, link):
    response = request_resource.get('https://dog.ceo/api/breed' + link)
    validate(instance=response.json(), schema=VALIDATION_LIST_ALL_BREAD_SCHEMA)


@pytest.mark.status_code
@pytest.mark.parametrize('link', ['s/list/all', 's/image/random', '/hound/images', '/hound/list'])
def test_status_code(request_resource, link):
    response = request_resource.get('https://dog.ceo/api/breed' + link)
    assert response.status_code == 200, 'Status code is not 200'


@pytest.mark.content_type
@pytest.mark.parametrize('link', ['s/list/all', 's/image/random', '/hound/images', '/hound/list'])
def test_content_type(request_resource, link):
    response = request_resource.get('https://dog.ceo/api/breed' + link)
    assert response.headers['Content-Type'] == 'application/json', 'Wrong type of response. Must be JSON!'


@pytest.mark.list_all_breeds
def test_list_all_breeds(request_resource):
    link = 'https://dog.ceo/api/breeds/list/all'
    assert request_resource.get(link).json() == LIST_ALL_BREAD_SCHEMA


@pytest.mark.single_random_image
def test_single_random_image(request_resource):
    link = 'https://dog.ceo/api/breeds/image/random'
    assert request_resource.get(link).json()['status'] == 'success'


@pytest.mark.multiple_random_image
@pytest.mark.parametrize('amount', [number for number in range(1, 51)])
def test_multiple_random_image(request_resource, amount):
    link = f'https://dog.ceo/api/breeds/image/random/{amount}/'
    assert len(request_resource.get(link).json()['message']) == amount


@pytest.mark.by_breed
def test_by_breed(request_resource):
    link = 'https://dog.ceo/api/breed/hound/images'
    assert request_resource.get(link).json() == BREAD_SCHEMA
