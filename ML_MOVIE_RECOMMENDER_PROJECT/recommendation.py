
import pandas as pd

def recommend(movie_name, movie_matrix, movie_stats):

    movie_ratings = movie_matrix[movie_name]

    similar_movies = movie_matrix.corrwith(movie_ratings)

    corr_movie = pd.DataFrame(
        similar_movies,
        columns=['Correlation']
    )

    corr_movie.dropna(inplace=True)

    corr_movie = corr_movie.join(
        movie_stats['num ratings']
    )

    recommendations = corr_movie[
        corr_movie['num ratings'] > 50
    ].sort_values(
        'Correlation',
        ascending=False
    )

    return recommendations.head(10)
