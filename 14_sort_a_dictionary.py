import json, pprint

with open(r"D:\Work\PythonSuli\kezdo-250111\alapok_2\movie_data.json") as f:
    movie_list = json.load(f)

sorted_movies = sorted(movie_list, key=lambda movie: movie["vote_average"], reverse=True)

for movie in sorted_movies:
    print(movie["title"], movie["vote_average"])