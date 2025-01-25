import json, os, pprint
import tmdbsimple as tmdb

tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"
tmdb.REQUESTS_TIMEOUT = 5

def main():
    os.system("cls")
    print("-"*50, "THE MOVIE DATABASE", "-"*50)
    
    page_number = int( input("Give me the page number: ") )
    movie_list = get_movies(page_number)
    print_movies(movie_list)

    response = input("Do you want to save this list? (y/n)")
    if response == "y":
        save_movies(movie_list)
    
    response = input("Do you want to run another request? (y/n)")
    if response == "y":
        main()

def get_movies(page_number: int):
    movies = tmdb.Movies()
    return movies.popular(page=page_number)["results"]

def print_movies(movie_list):
    for movie in movie_list:
        print(movie["title"], movie["vote_average"])

def save_movies(movie_list):
    with open("movie_database.json", "w") as f:
        json.dump(movie_list, f)

    print("Movie database saved.")

main()