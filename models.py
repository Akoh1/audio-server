# from app import db
from app import db
import datetime
import json


class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    audiotype = db.Column(db.String(50), default='song', nullable=False)
    uploaded = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        # self.audiotype = audiotype
        # self.uploaded = uploaded

    def __repr__(self):
        return '<id {}>'.format(self.name)

    def json(self):
        return {
            'id': self.id, 'name': self.name,
            'duration': self.duration, 'audiotype': self.audiotype,
            'uploaded': self.uploaded
        }

    def get_all_songs():
        '''function to get all movies in our database'''
        return [Song.json(song) for song in Song.query.all()]

    def get_song(id):
        '''function to get song using the id of the song as parameter'''
        return [Song.json(Song.query.filter_by(id=id).first())]
        

    def add_song(name, duration):
        song = Song(name=name, duration=duration
                    # audiotype=audiotype
                    )
        db.session.add(song)  
        db.session.commit()

    def update_song(id, name, duration):
        update = Song.query.filter_by(id=id).first()
        update.name = name
        update.duration = duration
        db.session.commit()
    
    def delete_song(id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        Song.query.filter_by(id=id).delete()
        # filter movie by id and delete
        db.session.commit()


class Podcast(db.Model):
    __tablename__ = 'podcasts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    audiotype = db.Column(db.String(50), default='podcast', nullable=False)
    uploaded = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    host = db.Column(db.String(100), nullable=False)

    def __init__(self, title, author, narrator, duration, host):
        self.title = title
        self.author = author
        self.narrator = narrator
        self.duration = duration
        # self.audiotype = audiotype
        # self.uploaded = uploaded
        self.host = host

    def __repr__(self):
        return '<id {}>'.format(self.title)

    def json(self):
        return {
            'id': self.id, 'title': self.title,
            'author': self.author, 'narrator': self.narrator,
            'duration': self.duration, 'audiotype': self.audiotype,
            'uploaded': self.uploaded, 'host': self.host
        }
    
    def get_all_podcast():
        '''function to get all movies in our database'''
        return [Podcast.json(podcast) for podcast in Podcast.query.all()]

    def get_podcast(id):
        '''function to get song using the id of the song as parameter'''
        return [Podcast.json(Podcast.query.filter_by(id=id).first())]
    
    def add_podcast(title, author, narrator, duration, host):
        podcast = Podcast(title=title, author=author, narrator=narrator, 
                         duration=duration, host=host)
        db.session.add(podcast)  
        db.session.commit()

    def update_podcast(id, title, author, narrator, duration, host):
        update = Podcast.query.filter_by(id=id).first()
        update.title = title
        update.author = author
        update.narrator = narrator
        update.duration = duration
        update.host = host
        db.session.commit()

    def delete_podcast(id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        Podcast.query.filter_by(id=id).delete()
        # filter movie by id and delete
        db.session.commit()


class Audiobook(db.Model):
    __tablename__ = 'audiobooks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    audiotype = db.Column(db.String(50), default='audiobook', nullable=False)
    uploaded = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title, author, narrator, duration):
        self.title = title
        self.author = author
        self.narrator = narrator
        self.duration = duration
        # self.audiotype = audiotype
        # self.uploaded = uploaded

    def __repr__(self):
        return '<id {}>'.format(self.title)

    def json(self):
        return {
            'id': self.id, 'title': self.title,
            'author': self.author, 'narrator': self.narrator,
            'duration': self.duration, 'audiotype': self.audiotype,
            'uploaded': self.uploaded
        }

    def get_all_audio():
        '''function to get all movies in our database'''
        return [Audiobook.json(audio) for audio in Audiobook.query.all()]

    def get_audio(id):
        '''function to get song using the id of the song as parameter'''
        return [Audiobook.json(Audiobook.query.filter_by(id=id).first())]

    def add_audio(title, author, narrator, duration):
        audio = Audiobook(title=title, author=author, narrator=narrator, 
                         duration=duration)
        db.session.add(audio)  
        db.session.commit()

    def update_audio(id, title, author, narrator, duration):
        update = Audiobook.query.filter_by(id=id).first()
        update.title = title
        update.author = author
        update.narrator = narrator
        update.duration = duration
        db.session.commit()

    def delete_audio(id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        Audiobook.query.filter_by(id=id).delete()
        # filter movie by id and delete
        db.session.commit()