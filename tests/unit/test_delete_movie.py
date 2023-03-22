# TODO: Feature 6
from src.repositories.movie_repository import get_movie_repository

def test_delete_movie():
    movie_repository = get_movie_repository()

    # Create a temporary movie to delete
    temp_movie = movie_repository.create_movie('Avengers Endgame', 'Russo Brothers', 5)
    movie_id = temp_movie.movie_id
    
    # Delete movie
    movie_repository.delete_movie(movie_id)

    # Check that the movie was deleted
    deleted_movie = movie_repository.get_movie_by_id(movie_id)
    assert deleted_movie is None
