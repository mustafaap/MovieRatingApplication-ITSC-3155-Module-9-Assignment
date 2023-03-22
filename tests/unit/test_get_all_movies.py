# TODO: Feature 1
from tests.e2e.conftest import test_app
from src.repositories.movie_repository import get_movie_repository

def test_get_all_movies(test_app):
    movie_rep = get_movie_repository()

    # Clear database
    movie_rep.clear_db()

    # Adds movies to database
    temp_movie1 = movie_rep.create_movie('Movie', 'Dude', 5)
    temp_movie2 = movie_rep.create_movie('Movie2', 'Guy', 3)

    # Use get_all_movies to get a dict of movies
    movie_dict = movie_rep.get_all_movies()

    # Make sure the length is correct
    assert len(movie_dict) == 2

    # Make sure the contents of the dict is correct
    assert temp_movie1.title == movie_dict[temp_movie1.movie_id].title
    assert temp_movie1.rating == movie_dict[temp_movie1.movie_id].rating
    assert temp_movie1.director == movie_dict[temp_movie1.movie_id].director
    assert temp_movie2.title == movie_dict[temp_movie2.movie_id].title
    assert temp_movie2.rating == movie_dict[temp_movie2.movie_id].rating
    assert temp_movie2.director == movie_dict[temp_movie2.movie_id].director
