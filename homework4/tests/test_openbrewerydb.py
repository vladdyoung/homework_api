import pytest


@pytest.mark.status_code
def test_status_code(request_resource):
    response = request_resource.get('https://api.openbrewerydb.org/breweries')
    assert response.status_code == 200, 'Status code is not 200'


@pytest.mark.content_type
def test_content_type(request_resource):
    response = request_resource.get('https://api.openbrewerydb.org/breweries')
    assert 'application/json' in response.headers['Content-Type'], 'Wrong type of response. Must be JSON!'


@pytest.mark.by_city
@pytest.mark.parametrize('city', ['san_diego', 'new_york', 'los_angeles'])
def test_browse_by_citi(request_resource, city):
    response = request_resource.get('https://api.openbrewerydb.org/breweries?by_city=' + city)
    assert len(response.json()) > 0, 'City is not found'


@pytest.mark.by_state
@pytest.mark.parametrize('state', ['ohio', 'new_york', 'new%20mexico'])
def test_browse_by_state(request_resource, state):
    response = request_resource.get('https://api.openbrewerydb.org/breweries?by_state=' + state)
    assert len(response.json()) > 0, 'State is not found'


@pytest.mark.by_type
@pytest.mark.parametrize('type', ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract',
                                  'proprietor', 'closed'])
def test_browse_by_type(request_resource, type):
    response = request_resource.get('https://api.openbrewerydb.org/breweries?by_type=' + type)
    assert len(response.json()) > 0, 'Type is not found'
