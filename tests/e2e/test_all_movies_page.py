
from tests.e2e.conftest import test_app
from src.repositories.movie_repository import get_movie_repository

def test_all_movies_page(test_app):
    movie_rep = get_movie_repository()

    # Clear database
    movie_rep.clear_db()

    # Get response data from list_all_movies page
    response = test_app.get('/movies')

    # Make sure the page is directed correctly
    assert response.status_code == 200

    # Test that the correct page was loaded using a part of the html file
    assert b'''<h1 class="mb-5">All Movies</h1>
<p class="mb-3">See our list of movie ratings below</p>
<table class="table">
<thead class="table-light">''' in response.data
    
    # Clear database
    movie_rep.clear_db()

