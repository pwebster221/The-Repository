import os
import logging

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Swiss Ephemeris Path
SWISSEPH_PATH = "/Users/dubtownraces/Documents/GitHub/The-Esoteric-Repository/Feeders/AstroAPI_Sub_Program/astroapi/swisseph/ephe"

# Neo4j Configuration
NEO4J_URI = "bolt://localhost:7687" if ENVIRONMENT == "development" else "bolt://production-db:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "your_neo4j_password"

# API Configuration
API_BASE_URL = "https://exampleapi.com/v1"
API_KEY = "your_api_key_here"

# Flask Configuration
SECRET_KEY = "your_flask_secret_key"
DEBUG = True if ENVIRONMENT == "development" else False

# Logging Configuration
LOG_LEVEL = logging.DEBUG if ENVIRONMENT == "development" else logging.ERROR
LOG_FILE = "astroapi.log"

# Paths
STATIC_PATH = "/path/to/static"
TEMPLATE_PATH = "/path/to/templates"

# Email Configuration
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USERNAME = "your_email@example.com"
MAIL_PASSWORD = "your_email_password"
MAIL_USE_TLS = True
MAIL_USE_SSL = False

# Redis or Cache Configuration
CACHE_TYPE = "redis"
CACHE_REDIS_URL = "redis://localhost:6379/0"

# Celery Configuration (if applicable)
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"