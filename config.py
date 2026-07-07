# ============================================================
# config.py
# ============================================================

import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# TMDB API Key
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# API URLs
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# Flask Secret Key
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "movie-recommender-secret-key"
)

# Number of recommendations to show
TOP_N_RECOMMENDATIONS = 10