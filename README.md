# Movie Recommendation System

This project is a web-based movie recommendation application built with Flask and Python. It allows users to search for a movie and receive a list of similar or likely-to-be-liked movies in a clean and interactive interface.

## What This Project Does

The application combines machine learning with a simple web experience to make movie suggestions more intelligent. Instead of showing random movies, it uses a hybrid recommendation approach that considers both:

- content similarity between movies
- collaborative filtering predictions based on learned patterns

This makes the recommendations more useful and relevant to the movie the user selects.

## Main Features

- Search for any movie by name
- Display recommendations for the selected movie
- Show trending movies on the homepage
- Provide search suggestions while typing
- Present results in a visually appealing movie card layout
- Offer a smooth user experience through a Flask-powered web interface

## How It Works

1. The user enters a movie name in the search box.
2. The Flask app receives the request and passes it to the recommendation engine.
3. The recommender loads a pretrained model and generates movie suggestions.
4. The results are displayed on the webpage as cards with movie details and scores.

## Project Structure

- `app.py` – Flask application and route handling
- `recommender.py` – Recommendation logic and model integration
- `templates/` – HTML pages for the web UI
- `static/` – CSS and JavaScript for styling and interactions
- `movie_recommender_model.pkl` – Pretrained recommendation model
- `requirements.txt` – Python dependencies

## Why This Project Is Useful

This project demonstrates how machine learning can be applied in a real-world web application. It is a beginner-friendly example of how recommendation systems work and how they can be presented through a user-friendly interface.

## Setup Steps

1. Install Python and create a virtual environment.
2. Install the required packages:
   `pip install -r requirements.txt`
3. Run the app:
   `python app.py`
4. Open the browser at:
   `http://127.0.0.1:5000/`