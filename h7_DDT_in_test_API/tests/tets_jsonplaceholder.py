import pytest


@pytest.mark.status_code
@pytest.mark.parametrize('resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
def test_status_code(request_resource, resource):
    response = request_resource.get('https://jsonplaceholder.typicode.com/'+resource)
    assert response.status_code == 200, 'Status code is not 200'


@pytest.mark.content_type
@pytest.mark.parametrize('resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
def test_content_type(request_resource, resource):
    response = request_resource.get('https://jsonplaceholder.typicode.com/'+resource)
    assert 'application/json' in response.headers['Content-Type'], 'Wrong type of response. Must be JSON!'


@pytest.mark.posts
@pytest.mark.parametrize('number', [number for number in range(1, 101)])
def test_number_posts(request_resource, number):
    response = request_resource.get(f'https://jsonplaceholder.typicode.com/posts/{number}')
    assert response.json()['id'] == number, 'Not found post'


@pytest.mark.posts
@pytest.mark.parametrize('number', [number for number in range(1, 501)])
def test_number_comments(request_resource, number):
    response = request_resource.get(f'https://jsonplaceholder.typicode.com/comments/{number}')
    assert response.json()['id'] == number, 'Not found comments'


@pytest.mark.creating_resource
def test_creating_resource_using_post(request_resource):
    data = {
                'title': 'foo',
                'body': 'bar',
                'userId': 1
            }
    response = request_resource.post('https://jsonplaceholder.typicode.com/posts', json=data)
    print(response.json())
    assert response.json()['id'] > 100 and response.json()['title'] == 'foo', 'Resource do not exists'


@pytest.mark.full_updete_resource
def test_full_update_resource_using_put(request_resource):
    data = {
                'title': 'updated',
                'body': 'updated'
            }
    before_update = request_resource.get('https://jsonplaceholder.typicode.com/posts/1')
    response = request_resource.put('https://jsonplaceholder.typicode.com/posts/1', data=data)
    assert response.json()['title'] != before_update.json()['title'], 'Resource do not update'


@pytest.mark.part_updete_resource
def test_part_update_resource_using_patch(request_resource):
    data = {
                'title': 'updated'
            }
    before_update = request_resource.get('https://jsonplaceholder.typicode.com/posts/2')
    response = request_resource.patch('https://jsonplaceholder.typicode.com/posts/2', data=data)
    print(before_update.json())
    print(response.json())
    assert response.json()['title'] != before_update.json()['title'], 'Resource do not update'


@pytest.mark.delete_resource
def test_delete_resource_using_delete(request_resource):
    request_delete = request_resource.delete('https://jsonplaceholder.typicode.com/posts/3')
    assert request_delete.status_code == 200, 'Resource do not delete'

