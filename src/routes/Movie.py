from flask import Blueprint, jsonify, request
import uuid
# entities
from models.entities.movie import Movie

# Models
from models.movieModel import MovieModel

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_movie():
    try:
        titulo = request.json['titulo']
        duracion = int(request.json['duracion'])
        fecha_estreno = request.json['fecha_estreno']
        id = uuid.uuid4()
        movie = Movie(str(id), titulo, duracion, fecha_estreno)

        affected_rows = MovieModel.add_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "Error on insert"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie=Movie(id)
        
        affected_rows = MovieModel.delete_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "no movie delete"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        titulo = request.json['titulo']
        duracion = int(request.json['duracion'])
        fecha_estreno = request.json['fecha_estreno']
        movie = Movie(id, titulo, duracion, fecha_estreno)

        affected_rows = MovieModel.update_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "no movie updated"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500