from .base import *

DEBUG = True

ALLOWED_HOSTS = ["18.216.104.88", "18.118.165.84"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASSWORD"),
        "HOST": env.str("DB_HOST"),
        "PORT": "5432",
    }
}

# Configuration CORS
CORS_ALLOWED_ORIGINS = [
    "http://18.216.104.88:8000",
    "http://18.118.165.84"
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "POST",
    "PUT",
    "PATCH",
)

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
