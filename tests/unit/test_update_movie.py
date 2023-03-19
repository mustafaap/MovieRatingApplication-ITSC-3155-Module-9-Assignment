# TODO: Feature 5

from tests.e2e.conftest import test_app
from src.repositories.movie_repository import get_movie_repository

def test_update_movie(test_app):
    movie_repository = get_movie_repository()
    temp_movie = movie_repository.create_movie('Avengers Endgame', 'Russo Brothers', 5)
    movie_id = temp_movie.movie_id
    updated_movie_data = {
        'title': 'Avengers: Endgame',
        'director': 'Russo Brothers',
        'rating': 4
    }
    response = test_app.post(f'/movies/{movie_id}', data=updated_movie_data)

    # Check that the response is a redirect to the single movie page
    assert response.status_code == 302 
    # Check that the movie was updated in the database
    updated_movie = movie_repository.get_movie_by_id(movie_id)
    assert updated_movie.title == updated_movie_data['title']
    assert updated_movie.director == updated_movie_data['director']
    assert updated_movie.rating == updated_movie_data['rating']