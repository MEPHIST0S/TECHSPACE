from app import app
from extensions import *
from app import *

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/search-by-title', methods=['GET'])
def search_by_title():
    title = request.args.get('t')
    year = request.args.get('y')
    plot = request.args.get('plot')

    movie = Movie.query.filter_by(title=title, year=year).first()

    return render_template('index.html', movie=movie, search_type='title')

@app.route('/search-by-id', methods=['GET'])
def search_by_id():
    movie_id = request.args.get('i')
    plot = request.args.get('plot')

    movie = Movie.query.get(movie_id)

    return render_template('index.html', movie=movie, search_type='id')