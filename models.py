"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    name = db.Column(db.String)

    desc = db.Column(db.Text)

    songs = db.relationship('Song',secondary='playsongs',backref='playlists')

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    title = db.Column(db.String)

    artist = db.Column(db.String)

    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playsongs'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    playlist_id = db.Column(db.Integer,db.ForeignKey('playlists.id'))

    song_id = db.Column(db.Integer,db.ForeignKey('songs.id'))

    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
