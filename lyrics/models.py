from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Song(db.Model):
    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(250), nullable=True)
    lyrics = db.Column(db.Text)
    cover = db.Column(db.Boolean)

    def __repr__(self):
        return '<Song:  {}>'.format(self.name)

class Writer(db.Model):
    __tablename__ = 'writer'

    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Writer: {}>'.format(self.name)

class Performer(db.Model):
    __tablename__ = 'performer'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Performer: {}>'.format(self.name)

class Album(db.Model):
    __tablename__ = 'album'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    year_released = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Album: {}>'.format(self.name)
