# TODO: Feature 6
from app import app
from src.repositories.movie_repository import get_movie_repository

test_app = app.test_client()

def test_delete_movie():

    # Create a temporary movie to delete
    movie_repository = get_movie_repository()
    temp_movie = movie_repository.create_movie('Avengers Endgame', 'Russo Brothers', 5)

    # Send a request to delete the movie
    response = test_app.post(f'/movies/{temp_movie.movie_id}/delete')

    # Check that the response is a redirect to the list all movies page
    assert response.status_code == 302 

    # Check that the movie was deleted from the database
    deleted_movie = movie_repository.get_movie_by_id(temp_movie.movie_id)
    assert deleted_movie is None
