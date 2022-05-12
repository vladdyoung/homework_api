def test_ya(request_resource, base_url, request_status_code):
    response = request_resource.get(base_url)
    assert response.status_code == int(request_status_code)
