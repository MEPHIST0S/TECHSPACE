import pymysql
import requests
import json

# CONNECTING TO DB MYSQL
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '4444',
    database = 'MOVIE_INFO',
    port = 3308,
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)
print(connection.host_info)

#EXTRACTING DATA
def get_movie_info(title):
    api_key = '5d9df2b8'
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    if data['Response'] == 'True':
        return {
            'title': data.get('Title'),
            'released': data.get('Released'),
            'genre': data.get('Genre'),
            'director': data.get('Director')
        }
    else:
        print("Not Found")
        return None

title = str(input())
movie = get_movie_info(title)
print(movie)

def save_movie_to_db(movie):
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO MOVIE_INFO (title, released, genre, director) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (movie['title'], movie['released'], movie['genre'], movie['director']))
        connection.commit()

if movie:
    save_movie_to_db(movie)