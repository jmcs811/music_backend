from typing import List, Optional

from pydantic import BaseModel

class TrackBase(BaseModel):
    name: str
    filename: str
    duration_ms: int
    track_number: int

class TrackCreate(TrackBase):
    pass

class Track(TrackBase):
    song_id: int
    album_id: int
    artist_id: int

    class Config:
        orm_mode = True

class AlbumBase(BaseModel):
    name: str
    release_date: str
    album_art: str

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    album_id: int
    artist_id: int
    albums: List[Track] = []


class ArtistBase(BaseModel):
    name: str

class ArtistCreate(TrackBase):
    pass

class Artist(BaseModel):
    artist_id: int
    albums: List[Album] = []

    class Config:
        orm_mode = True
