from flask import Flask, render_template, request, jsonify

from recommender import MovieRecommender

app = Flask(__name__)
model = MovieRecommender()

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    movie_name = request.form.get("movie")

    if not movie_name:

        return jsonify({
            "status": "error",
            "message": "Movie name required"
        })

    selected_movie = None
    idx = model.get_index(movie_name)

    if idx is not None:
        selected_movie = model.movie_details(idx)
        selected_movie["score"] = 1.0
        selected_movie["is_selected"] = True

    recommendations = model.hybrid_recommend(
        movie_name,
        user_id=1,
        top_n=10
    )

    if selected_movie is not None:
        recommendations = [selected_movie] + recommendations

    if len(recommendations) == 0:

        return jsonify({

            "status": "error",

            "message": "Movie not found"

        })

    return jsonify({

        "status": "success",

        "movie": movie_name,

        "recommendations": recommendations

    })

@app.route("/trending")
def trending():

    top_movies = model.movies.sort_values(
        by=["vote_average", "popularity"],
        ascending=False
    ).head(12)

    results = []

    for _, movie in top_movies.iterrows():

        results.append({

            "title": movie["title_ml"],

            "rating": float(movie["vote_average"]),

            "genres": movie["genres_tmdb"],

            "director": movie["director"],

            "overview": (
                " ".join(movie["overview"])
                if isinstance(movie["overview"], list)
                else movie["overview"]
            )

        })

    return jsonify(results)

@app.route("/search")
def search():

    query = request.args.get("q", "")

    suggestions = model.search_suggestions(query)

    return jsonify(suggestions)


if __name__ == "__main__":

    app.run(
        debug=True
    )