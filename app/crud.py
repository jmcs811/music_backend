from sqlalchemy.orm import Session

import schemas
import models

def get_songs(db: Session):
    return db.query(models.Track).all()

def get_song(db: Session, song_id: int):
    return db.query(models.Track).filter(models.Track.song_id == song_id).first()

def get_artists(db: Session):
    print("getting artist")
    return db.query(models.Artist).all()

def get_artist(db: Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.artist_id == artist_id).first()

def get_albums(db: Session):
    return db.query(models.Album).all()

def get_album(db: Session, album_id: int):
    return db.query(models.Track).filter(models.Track.album_id == album_id).all()