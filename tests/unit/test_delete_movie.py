# TODO: Feature 6
from tests.e2e.conftest import test_app
from src.repositories.movie_repository import get_movie_repository

def test_delete_movie(test_app):
    movie_repository = get_movie_repository()
    temp_movie = movie_repository.create_movie('Avengers Endgame', 'Russo Brothers', 5)
    movie_id = temp_movie.movie_id
    response = test_app.post(f'/movies/{movie_id}/delete')

    # Check that the response is a redirect to the list all movies page
    assert response.status_code == 302 
    # Check that the movie was deleted from the database
    deleted_movie = movie_repository.get_movie_by_id(movie_id)
    assert deleted_movie is None
