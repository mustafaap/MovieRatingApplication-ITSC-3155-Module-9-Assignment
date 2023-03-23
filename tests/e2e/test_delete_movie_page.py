# TODO: Feature 6
from app import app
from src.repositories.movie_repository import get_movie_repository

test_app = app.test_client()

def test_delete_movie():

    movie_repository = get_movie_repository()
    # Clear database
    movie_repository.clear_db()

    # Create a temporary movie to delete
    temp_movie1 = movie_repository.create_movie('Avengers Endgame', 'Russo Brothers', 5)
    temp_movie2 = movie_repository.create_movie('Avengers Infinity war', 'Russo Brothers', 4)
    temp_movie3 = movie_repository.create_movie('The Avengers', 'Joss Whedon', 4)

    # Adding movie to database
    movie_repository._db[0] = temp_movie1
    movie_repository._db[1] = temp_movie2
    movie_repository._db[2] = temp_movie3

    # Send a request to delete the movie
    response = test_app.post(f'/movies/{temp_movie1.movie_id}/delete')
    response = test_app.post(f'/movies/{temp_movie2.movie_id}/delete')

    # Check that the response is a redirect to the list all movies page
    assert response.status_code == 302 

    # Check that the movie was deleted from the database
    deleted_movie1 = movie_repository.get_movie_by_id(temp_movie1.movie_id)
    deleted_movie2 = movie_repository.get_movie_by_id(temp_movie2.movie_id)

    # Check that the movie was not deleted from the dateabase
    deleted_movie3 = movie_repository.get_movie_by_id(temp_movie3.movie_id)

    assert deleted_movie1 is None
    assert deleted_movie2 is None
    assert deleted_movie3 is not None