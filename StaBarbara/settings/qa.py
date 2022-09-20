from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

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
    "http://54.152.3.65:8000",
    "http://50.17.14.2"
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
