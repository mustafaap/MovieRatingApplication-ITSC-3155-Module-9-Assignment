# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_get_movie_by_id():
    test_movie = movie_repository.create_movie("Avengers Endgame", "Russo Brothers", 5)
    movie_id = test_movie.movie_id
    
    assert movie_repository.get_movie_by_id(test_movie.movie_id) == test_movie
    assert movie_repository.get_movie_by_id(test_movie.movie_id).movie_id == movie_id