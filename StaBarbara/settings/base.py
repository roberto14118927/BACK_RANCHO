from pathlib import Path
import os
import django_heroku
import environ


# Initialise environment variables
env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECRET_KEY = 'django-insecure-kqs%pnac-lx%08o1!b@-^fk1k(f#0@4x^&k7fwa*czoe^aw-7#'
SECRET_KEY = env.str('SECRET_KEY', '123')

# Application definition
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


LOCAL_APPS = [ 
    'apps.base',
    'apps.Ganado.Control_Ganado',
    'apps.Ganado.Control_Peso',
    'apps.Ganado.Control_Empadre',

    'apps.Inventarios.Control_Termocrio',
    'apps.Inventarios.Control_IAlimentos',
    'apps.Inventarios.Control_IMedicos',
    'apps.Inventarios.Control_IMateriales',
    'apps.Inventarios.Control_Vacunacion',
    'apps.Inventarios.Control_Desparasitacion',

    'apps.Users.Control_Medicos',
    'apps.Users.Control_Usuario',
    'apps.Users.Control_Login',
    'apps.Users.Control_Notificacion',
]


THIRD_APPS = [
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'corsheaders'
]


INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

#Para agregar quitar los permisos de autenticación, comentar los primeros 3.
#De igual manera, se debe quitar de las vistas los permisos de autenticación. 

REST_FRAMEWORK = {
    #'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.IsAuthenticated',),
    #'DEFAULT_AUTHENTICATION_CLASSES':('rest_framework.authentication.TokenAuthentication'),
    #'rest_framework.authentication.SessionAuthentication',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}


#El token expira en  minutos
TOKEN_EXPIRED_AFTER_SECONDS = 86400


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'StaBarbara.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            },
        },
    },
]

WSGI_APPLICATION = 'StaBarbara.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'

#Set default model user
AUTH_USER_MODEL = 'Control_Usuario.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#Activating django heroku
django_heroku.settings(locals())
