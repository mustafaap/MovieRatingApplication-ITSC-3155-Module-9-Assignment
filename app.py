from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

from src.models.movie import Movie
app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()
#tempmovie = movie_repository.create_movie("Avengers Endgame", "Russo Brothers", 5)
#movie_repository._db[0] = tempmovie
#movie2 = movie_repository.create_movie("New Movie", "New Director", 3)
#movie_repository._db[1] = movie2

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    return render_template('list_all_movies.html', list_movies_active=True, movie_dict = movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    
    movie_name = request.form.get('name')
    director = request.form.get('director')
    rating = int(request.form.get('rating'))
    movie_repository.create_movie(movie_name, director, rating)
    return redirect('/movies')


@app.get('/movies/search/')
def search_movies():
        title = request.args.get('title')
        movies = movie_repository.get_movie_by_title(title)
        return render_template('search_movies.html', movies = movies, search_active=True, title=title)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', movie=movie, movie_id=movie_id)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('edit_movies_form.html', movie=movie)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    title = request.form['title']
    director = request.form['director']
    rating = int(request.form['rating'])
    movie_repository.update_movie(movie_id, title, director, rating)
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    movie_repository.delete_movie(movie_id)
    return redirect('/movies')
 