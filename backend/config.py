# backend/config.py
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

class Settings:
    GOOGLE_MAPS_API_KEY = GOOGLE_MAPS_API_KEY

settings = Settings()
