from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from env import SPOTIFY_ALBUMS, SPOTIFY_ARTISTS, SPOTIFY_SONGS

from database import Base

class Track(Base):
    __tablename__ = SPOTIFY_SONGS

    song_id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey(f"{SPOTIFY_ALBUMS}.album_id"))
    artist_id = Column(Integer, ForeignKey(f"{SPOTIFY_ARTISTS}.artist_id"))
    name = Column(String(50))
    filename = Column(String(255))
    duration_ms = Column(Integer)
    track_number = Column(Integer)
    artist = relationship("Artist", backref="Track")


class Artist(Base):
    __tablename__ = SPOTIFY_ARTISTS

    artist_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    track_info = relationship("Track", back_populates="artist")


class Album(Base):
    __tablename__ = SPOTIFY_ALBUMS

    album_id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, ForeignKey(f"{SPOTIFY_ARTISTS}.artist_id"))
    name = Column(String(50))
    release_date = Column(String(50)) # maybe an issue, datetime
    album_art = Column(String(255))

