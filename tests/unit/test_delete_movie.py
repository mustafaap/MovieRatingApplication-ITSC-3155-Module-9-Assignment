# TODO: Feature 6
from src.repositories.movie_repository import get_movie_repository

def test_delete_movie():
    movie_repository = get_movie_repository()

    # Create a temporary movie to delete
    temp_movie1 = movie_repository.create_movie('Avengers Endgame', 'Russo Brothers', 5)
    temp_movie2 = movie_repository.create_movie('Avengers Infinity war', 'Russo Brothers', 4)
    temp_movie3 = movie_repository.create_movie('The Avengers', 'Joss Whedon', 4)

    movie_id1 = temp_movie1.movie_id
    movie_id2 = temp_movie2.movie_id
    movie_id3 = temp_movie3.movie_id

    # Delete movie
    movie_repository.delete_movie(movie_id1)
    movie_repository.delete_movie(movie_id2)

    # Check that the movie was deleted
    deleted_movie1 = movie_repository.get_movie_by_id(movie_id1)
    assert deleted_movie1 is None

    # Check that the movie was deleted
    deleted_movie2 = movie_repository.get_movie_by_id(movie_id2)
    assert deleted_movie2 is None

    # Check that the movie was not deleted
    deleted_movie3 = movie_repository.get_movie_by_id(movie_id3)
    assert deleted_movie3 is not None
