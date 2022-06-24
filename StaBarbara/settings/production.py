from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "https://santabarbara-back.herokuapp.com",
]

# Set database config
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'rancho',
#         'USER': 'ranchouser',
#         'PASSWORD': 'admin',
#         'HOST': 'postgres',
#         'PORT': '5432',
#     }
# }

#Configuration CORS 
CORS_ALLOWED_ORIGINS  = [
     "https://santabarbara-back.herokuapp.com",
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

