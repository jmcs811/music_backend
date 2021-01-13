from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import crud, models
from database import SessionLocal, engine

from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.mount("/data", StaticFiles(directory="data"), name="static")

origins = [
    "http://localhost.com",
    "https://localhost.com",
    "http://localhost.com:8000",
    "https://localhost.com:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message":"Hello, world"}

@app.get("/tracks")
def tracks(db: Session = Depends(get_db)):
    db_tracks = crud.get_songs(db)
    if db_tracks is None:
        raise HTTPException(status_code=404, detail="No songs")
    return db_tracks

@app.get("/track/{track_id}")
def get_track(track_id: int, db: Session = Depends(get_db)):
    db_track = crud.get_song(db, song_id=track_id)
    if db_track is None:
        raise HTTPException(status_code=404, detail="Track not found")
    return db_track

@app.get("/artists")
async def artists(db: Session = Depends(get_db)):
    db_artist = crud.get_artists(db)
    if db_artist is None:
        raise HTTPException(status_code=404, detail="No artists")
    return db_artist

@app.get("/artist/{artist_id}")
def get_artist(artist_id: int, db: Session = Depends(get_db)):
    db_artist = crud.get_artist(db, artist_id=artist_id)
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db_artist

@app.get("/albums")
def albums(db: Session = Depends(get_db)):
    db_albums = crud.get_albums(db)
    if db_albums is None:
        raise HTTPException(status_code=404, detail="No albums")
    return db_albums

@app.get("/album/{album_id}/tracks")
def get_album_tracks(album_id: int, db: Session = Depends(get_db)):
    db_album = crud.get_album(db, album_id=album_id)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album
    
    