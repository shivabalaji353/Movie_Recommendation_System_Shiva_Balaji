import pickle
import difflib
import numpy as np
import pandas as pd


class MovieRecommender:

    def __init__(self, model_path="movie_recommender_model.pkl"):

        with open(model_path, "rb") as f:
            model = pickle.load(f)

        self.movies = model["movies"]

        self.similarity = model["similarity"]

        self.svd = model["svd"]

        self.genre_mlb = model["genre_mlb"]

        self.cast_mlb = model["cast_mlb"]

        self.director_mlb = model["director_mlb"]

        self.tfidf_keywords = model["tfidf_keywords"]

        self.tfidf_overview = model["tfidf_overview"]

        self.title_column = "title_ml"

        self.movie_titles = self.movies[self.title_column].tolist()

    def search_movie(self, movie_name):

        matches = difflib.get_close_matches(
            movie_name,
            self.movie_titles,
            n=1,
            cutoff=0.5
        )

        if len(matches) == 0:
            return None

        return matches[0]

    def get_index(self, movie_name):

        movie = self.search_movie(movie_name)

        if movie is None:
            return None

        idx = self.movies[
            self.movies[self.title_column] == movie
        ].index[0]

        return idx

    def movie_details(self, idx):

        movie = self.movies.iloc[idx]

        def to_native(value):
            if isinstance(value, (np.integer,)):
                return int(value)
            if isinstance(value, (np.floating,)):
                return float(value)
            if isinstance(value, np.ndarray):
                return value.tolist()
            if isinstance(value, (list, tuple)):
                return [to_native(item) for item in value]
            if isinstance(value, dict):
                return {key: to_native(item) for key, item in value.items()}
            return value

        return {

            "movieId":
            to_native(movie["movieId"]),

            "tmdb_id":
            to_native(movie["tmdb_id"]),

            "title":
            to_native(movie["title_ml"]),

            "overview":
            " ".join(movie["overview"])
            if isinstance(movie["overview"], list)
            else to_native(movie["overview"]),

            "genres":
            to_native(movie["genres_tmdb"]),

            "director":
            to_native(movie["director"]),

            "vote_average":
            to_native(movie["vote_average"]),

            "popularity":
            to_native(movie["popularity"])

        }

    def content_recommend(self,
                          movie_name,
                          top_n=10):

        idx = self.get_index(movie_name)

        if idx is None:
            return []

        similarity_scores = list(
            enumerate(
                self.similarity[idx]
            )
        )

        similarity_scores = sorted(

            similarity_scores,

            key=lambda x: x[1],

            reverse=True

        )

        recommendations = []

        for i, score in similarity_scores[1:top_n+1]:

            movie = self.movie_details(i)

            movie["score"] = round(float(score), 3)

            recommendations.append(movie)

        return recommendations

    def hybrid_recommend(
            self,
            movie_name,
            user_id=1,
            top_n=10):

        idx = self.get_index(movie_name)

        if idx is None:
            return []

        similarity_scores = list(
            enumerate(
                self.similarity[idx]
            )
        )

        similarity_scores = sorted(

            similarity_scores,

            key=lambda x: x[1],

            reverse=True

        )

        recommendations = []

        for movie_index, sim_score in similarity_scores[1:80]:

            movie = self.movies.iloc[movie_index]

            movie_id = movie["movieId"]

            predicted = self.svd.predict(
                user_id,
                movie_id
            ).est

            hybrid_score = (

                0.60 * sim_score +

                0.40 * (predicted / 5)

            )

            recommendations.append(

                (

                    movie_index,

                    hybrid_score

                )

            )

        recommendations = sorted(

            recommendations,

            key=lambda x: x[1],

            reverse=True

        )[:top_n]

        results = []

        for movie_index, score in recommendations:

            movie = self.movie_details(movie_index)

            movie["score"] = round(float(score), 3)

            results.append(movie)

        return results

    # ========================================================
    # Search Suggestions
    # ========================================================

    def search_suggestions(
            self,
            text,
            limit=8):

        text = text.lower()

        suggestions = []

        for title in self.movie_titles:

            if text in title.lower():

                suggestions.append(title)

        return suggestions[:limit]