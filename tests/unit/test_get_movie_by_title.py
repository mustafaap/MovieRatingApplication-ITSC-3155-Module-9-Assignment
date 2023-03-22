# TODO: Feature 3
from tests.e2e.conftest import test_app
from src.repositories.movie_repository import get_movie_repository

def test_search_movies(test_app):
    movie_rep = get_movie_repository()
    # Clear database
    movie_rep.clear_db()
    # Adds movies to database
    temp_movie1 = movie_rep.create_movie('Avengers', 'Bill', 5)
    # Search for the movie by title
    response = test_app.get('/movies/search?title=Avengers')
    # Check if the response has the correct status code
    assert response.status_code == 200
    # Check if the returned HTML contains the movie's title and director
    assert temp_movie1.title in response.data.decode('utf-8')
    # Clear database
    movie_rep.clear_db()
