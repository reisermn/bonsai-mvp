"""Class-based Flask app configuration."""
from environs import Env

env = Env()
env.read_env()


class Config:
    """Configuration from environment variables."""

    SECRET_KEY = env.str("SECRET_KEY")
    # FLASK_ENV = env.str("FLASK_ENV")
    # FLASK_APP = "wsgi.py"

    MONGODB_HOST = env.str("MONGODB_URI")
    MONGO_URI = env.str("MONGODB_URI")

    # Static Assets
    # STATIC_FOLDER = "static"
    # TEMPLATES_FOLDER = "templates"
    # COMPRESSOR_DEBUG = True