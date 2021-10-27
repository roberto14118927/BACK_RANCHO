from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.models import User
from django.contrib.auth import login , logout 
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documentacion', schema_view),

    #control de ganado
    path(r'api/cows/' , include('apps.Ganado.Control_Ganado.urls')),
    path(r'api/peso/' , include('apps.Ganado.Control_Peso.urls')),
    path(r'api/empadre/' , include('apps.Ganado.Control_Empadre.urls')),

    #Control de inventarios
    path(r'api/termocrio/', include('apps.Inventarios.Control_Termo.urls')),
    path(r'api/inv/' , include('apps.Inventarios.Control_IAlimentos.urls')),
    path(r'api/inv/' , include('apps.Inventarios.Control_IMedicos.urls')),
    path(r'api/inv/' , include('apps.Inventarios.Control_IMateriales.urls')),

    #Control de usuarios
    path(r'api/medicos/', include('apps.Users.Control_Medicos.urls')),
    
    #Login
]
