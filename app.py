from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from decouple import config

app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config.from_object(config('APP_SETTINGS'))
app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# from models import Song, Audiobook, Podcast
from models import Song, Audiobook, Podcast
# from .models import Song, Audiobook, Podcast

# route to get all movies
@app.route('/<string:audioFileType>', methods=['GET'])
def get_audio(audioFileType):
    '''Function to get all the movies in the database'''
    if audioFileType == 'song':
        return jsonify({'Song': Song.get_all_songs()})
    elif audioFileType == 'podcast':
        return jsonify({'Podcast': Podcast.get_all_podcast()})
    elif audioFileType == 'audiobook':
        return jsonify({'Audiobook': Audiobook.get_all_audio()})
    else:
        return jsonify({'Error': 'Wrong Audio type'})

@app.route('/<string:audioFileType>/<int:audioFileID>', methods=['GET'])
def get_audio_by_id(audioFileType, audioFileID):
    if audioFileType == 'song':
        return_value = Song.get_song(audioFileID)
    elif audioFileType == 'podcast':
        return_value = Podcast.get_podcast(audioFileID)
    elif audioFileType == 'audiobook':
        return_value = Audiobook.get_audio(audioFileID)
    else:
        return_value = None
    return jsonify(return_value)

# route to add new movie
@app.route('/<string:audioFileType>', methods=['POST'])
def add_audio(audioFileType):
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    print(request_data)
    print("Check data")
    if audioFileType == 'song':
        print("I am song")
        Song.add_song(request_data["name"], request_data["duration"]
                    #   request_data["audioFileType"]
                      )
        response = Response("Song added", 201, mimetype='application/json')
    elif audioFileType == 'podcast':
        print("I am podcast")
        Podcast.add_podcast(request_data["title"], request_data["author"],
                         request_data["narrator"], request_data["duration"],
                         request_data["host"]
                    #   request_data["audioFileType"]
                      )
        response = Response("Podcast added", 201, mimetype='application/json')
    elif audioFileType == 'audiobook':
        print("I am audiobook")
        Audiobook.add_audio(request_data["title"], request_data["author"],
                         request_data["narrator"], request_data["duration"],
                    #   request_data["audioFileType"]
                      )
        response = Response("AudioBook added", 201, mimetype='application/json')
    else:
        response = Response("The request is invalid, not audio type", 400, mimetype='application/json')

    return response

@app.route('/<string:audioFileType>/<int:audioFileID>', methods=['PUT'])
def update_audio(audioFileType, audioFileID):
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    print(request_data)
    print("Check update data")
    if audioFileType == 'song':
        print("I am song")
        Song.update_song(audioFileID, request_data["name"], request_data["duration"]
                    #   request_data["audioFileType"]
                      )
        response = Response("Song updated", 201, mimetype='application/json')
    elif audioFileType == 'podcast':
        print("I am podcast")
        Podcast.update_podcast(audioFileID, request_data["title"], request_data["author"],
                         request_data["narrator"], request_data["duration"],
                         request_data["host"]
                    #   request_data["audioFileType"]
                      )
        response = Response("Podcast Updated", 201, mimetype='application/json')
    elif audioFileType == 'audiobook':
        print("I am audiobook")
        Audiobook.update_audio(audioFileID, request_data["title"], request_data["author"],
                         request_data["narrator"], request_data["duration"],
                    #   request_data["audioFileType"]
                      )
        response = Response("AudioBook Updated", 201, mimetype='application/json')
    else:
        response = Response("The request is invalid, not audio type", 400, mimetype='application/json')

    return response

@app.route('/<string:audioFileType>/<int:audioFileID>', methods=['DELETE'])
def remove_movie(audioFileType, audioFileID):
    '''Function to delete movie from our database'''
    if audioFileType == 'song':
        Song.delete_song(audioFileID)
        response = Response("Song Deleted", status=200, mimetype='application/json')
    elif audioFileType == 'podcast':
        Podcast.delete_podcast(audioFileID)
        response = Response("Podcast Deleted", status=200, mimetype='application/json')
    elif audioFileType == 'audiobook':
        Audiobook.delete_audio(audioFileID)
        response = Response("AudioBook Deleted", status=200, mimetype='application/json')
    else:
        response = Response("The request is invalid, not audio type", 400, mimetype='application/json')
    return response

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route("/name/<name>")
# def get_book_name(name):
#     return "name : {}".format(name)

# @app.route("/details")
# def get_book_details():
#     author=request.args.get('author')
#     published=request.args.get('published')
#     return "Author : {}, Published: {}".format(author,published)

if __name__ == '__main__':
    app.run()