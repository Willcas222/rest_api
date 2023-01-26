from database.db import get_connection
from .entities.movie import Movie


class MovieModel():
    
    @classmethod
    def get_movies(self):
        try:
            connection = get_connection()
            movies = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, titulo, duracion, fecha_sale FROM movie ORDER BY titulo ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())
                    
            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)
