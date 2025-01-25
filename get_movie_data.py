import json, os, pprint
import tmdbsimple as tmdb

tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"
tmdb.REQUESTS_TIMEOUT = 5

def main(page_number):
    movie_list = get_movies(page_number)
    print_movies(movie_list)
    save_movies(movie_list)

def get_movies(page_number):
    movies = tmdb.Movies()
    return movies.popular(page=page_number)["results"]

def print_movies(movie_list):
    pass

def save_movies(movie_list):
    pass


main(page_number=1)