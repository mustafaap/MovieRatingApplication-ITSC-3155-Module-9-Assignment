# TODO: Feature 2

def test_create_movie(test_app):
    response = test_app.post('/movies', data = {
        'name': 'Harry Potter',
        'director': 'JK Rowling',
        'rating': 5
    }, follow_redirects = True)

    data = response.data.decode('utf-8')

    assert response.status_code == 200

    assert '<td>Harry Potter</td>' in data
    assert '<td>JK Rowling</td>' in data
    assert '<td>5</td>' in data

def test_create_movie_validation_error(test_app):
    response = test_app.post('/movies')
    
    assert response.status_code == 400