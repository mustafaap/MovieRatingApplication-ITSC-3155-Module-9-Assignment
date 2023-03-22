# TODO: Feature 3
from tests.e2e.conftest import test_app
from src.repositories.movie_repository import get_movie_repository

def test_search_movies_page(test_app):
    movie_rep = get_movie_repository()

    # Clear database
    movie_rep.clear_db()

    # Create some movies to search for
    movie1 = movie_rep.create_movie('The Shawshank Redemption', 'Frank Darabont', 5)
    movie2 = movie_rep.create_movie('The Godfather', 'Francis Ford Coppola', 5)
    movie3 = movie_rep.create_movie('The Dark Knight', 'Christopher Nolan', 4)

    # Test searching for existing movie
    response = test_app.get('/movies/search?title=The Shawshank Redemption')
    assert response.status_code == 200
    assert b'<td>The Shawshank Redemption</td>' in response.data
    assert b'<td>Frank Darabont</td>' in response.data
    assert b'<td>5</td>' in response.data

    # Test searching for non-existent movie
    response = test_app.get('/movies/search?title=Interstellar')
    assert response.status_code == 200
    assert b'<p>No results found for "Interstellar".</p>' in response.data

    # Clear database
    movie_rep.clear_db()
