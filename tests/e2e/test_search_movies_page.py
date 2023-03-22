# TODO: Feature 3
from tests.e2e.conftest import test_app
from src.repositories.movie_repository import get_movie_repository

def test_search_movies_page(test_app):
    movie_rep = get_movie_repository()
    # Clear database
    movie_rep.clear_db()
    # Create some movies to search for
    movie1 = movie_rep.create_movie('Cars','John', 5)
    # Test searching for movie
    response = test_app.get('/movies/search?title=Cars')
    assert response.status_code == 200
    assert b'<li class="list-group-item">Cars</li>' in response.data
    # Clear database
    movie_rep.clear_db()
