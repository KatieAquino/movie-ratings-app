"""Script to see database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('drobdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

#load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

#create movies, store them in list to use
#to create fake ratings

movies_in_db = []
for movie in movie_data:
    #Get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime

    title, overview, poster_path = (movie['title'],
                                    movie['overview'],
                                    movie['poster_path'])

    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    # Create a movie here and append it to movies_in_db
    movie_entry = crud.create_movie(title, overview, release_date, poster_path)

    movies_in_db.append(movie_entry)