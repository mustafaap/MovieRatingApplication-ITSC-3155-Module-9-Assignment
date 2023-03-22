# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_view_movie_page(test_app):
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    tempmovie = movie_repository.create_movie("Avengers Endgame", "Russo Brothers", 5)
    movie_repository._db[0] = tempmovie

    response = test_app.get('/movies/0')

    assert response.status_code == 200
    assert '''<ul class="list-group">
            <li class="list-group-item">Avengers Endgame</li>
            <li class="list-group-item">Russo Brothers</li>
            <li class="list-group-item">5 / 5</li>
        </ul>'''.strip() in response.data.decode('utf-8').strip()
