from typing import List, Optional

from pydantic import BaseModel

class Track(BaseModel):
    song_id: int
    album_id: int
    artist_id: int
    name: str
    filename: str
    duration_ms: int
    track_number: int
    
    class Config:
        orm_mode = True

class Album(BaseModel):
    name: str
    release_date: str
    album_art: str
    album_id: int
    artist_id: int
    albums: List[Track] = []

class Artist(BaseModel):
    name: str
    artist_id: int
    albums: List[Album] = []

    class Config:
        orm_mode = True