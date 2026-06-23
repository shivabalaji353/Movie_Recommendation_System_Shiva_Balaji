
import pandas as pd

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

movie_data = pd.merge(
    ratings,
    movies,
    on="movieId"
)

print(movie_data.head())
