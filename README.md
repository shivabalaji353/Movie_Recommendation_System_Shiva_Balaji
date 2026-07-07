# Movie Recommendation System

A Flask-based movie recommendation application that suggests films based on a user’s selected movie. It combines content-based similarity with collaborative filtering to produce relevant recommendations.

## Features

- Search for a movie and see recommendations instantly
- Display the selected movie first in the recommendation list
- View trending movies and search suggestions
- Clean web interface with responsive styling

## Project Structure

- app.py — Flask routes and app setup
- recommender.py — recommendation logic and movie lookup
- static/ — CSS and JavaScript assets
- templates/ — HTML templates for the web UI
- movie_recommender_model.pkl — trained recommendation model

## Setup

1. Create and activate a virtual environment
2. Install dependencies: pip install -r requirements.txt
3. Run the app: python app.py
4. Open http://127.0.0.1:5000/ in your browser
