# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_view_movie_page(test_app):
    movie_repository = get_movie_repository()
    tempmovie = movie_repository.create_movie("Avengers Endgame", "Russo Brothers", 5)
    movie_repository._db[0] = tempmovie
    movie2 = movie_repository.create_movie("New Movie", "New Director", 3)
    movie_repository._db[1] = movie2

    response = test_app.get('/movies/0')

    assert response.status_code == 200
    assert '''<ul class="list-group">
            <li class="list-group-item">Avengers Endgame</li>
            <li class="list-group-item">Russo Brothers</li>
            <li class="list-group-item">5 / 5</li>
        </ul>'''.strip() in response.data.decode('utf-8').strip()
    assert '''<form action="/movies/0/edit" method="GET">
            <button type="submit" class="btn btn-primary">Edit Movie</button>
        </form>'''.strip() in response.data.decode('utf-8').strip()

    
    response2 = test_app.get('/movies/1')

    assert response2.status_code == 200
    assert '''<ul class="list-group">
            <li class="list-group-item">New Movie</li>
            <li class="list-group-item">New Director</li>
            <li class="list-group-item">3 / 5</li>
        </ul>'''.strip() in response2.data.decode('utf-8').strip()
    assert '''<form action="/movies/1/delete" method="POST">
            <button type="submit" class="btn btn-primary">Delete Movie</button>
        </form>'''.strip() in response2.data.decode('utf-8').strip()