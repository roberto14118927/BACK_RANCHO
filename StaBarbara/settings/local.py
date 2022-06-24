from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000'

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rancho',
        'USER': 'ranchouser',
        'PASSWORD': 'admin',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

#Configuration CORS 
CORS_ALLOWED_ORIGINS  = [
     'http://127.0.0.1:8000',
     'http://localhost:8000'
]

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'POST',
    'PUT',
    'PATCH',
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
