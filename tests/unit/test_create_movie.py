# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_create_movie():
    temp_movie = movie_repository.create_movie('Harry Potter', 'JK Rowling', 5)
    assert temp_movie.title == 'Harry Potter'
    assert temp_movie.director == 'JK Rowling'
    assert temp_movie.rating == 5

