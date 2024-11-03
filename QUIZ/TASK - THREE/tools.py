from app import app
from extensions import *
from app import *
from models import *

@app.route('/')
@app.route('/movies/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/movies/<int:movie_id>/')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movie.html', movie=movie)