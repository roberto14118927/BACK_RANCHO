from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from apps.Users.Control_Login.views import Login , Logout , UserToken


urlpatterns = [
    #Django admin
    path('admin/', admin.site.urls),
    #lOGIN
    path('login/' , Login.as_view()),
    path('logout/', Logout.as_view()),
    path('refresh-token/' , UserToken.as_view()),
    #viewsets
    path('usuario/', include("apps.Users.Control_Usuario.api.routers")),
    path('api/' , include('apps.Ganado.Control_Peso.api.routers')),
    path('api/' , include('apps.Ganado.Control_Ganado.api.routers')),
    path('api/' , include('apps.Ganado.Control_Empadre.api.routers')),
    path('api/' , include('apps.Inventarios.Control_IAlimentos.api.routers')),
    path('api/' , include('apps.Inventarios.Control_IMateriales.api.routers')), 
    path('api/' , include('apps.Inventarios.Control_IMedicos.api.routers')), 
    path('api/' , include('apps.Inventarios.Control_Termocrio.api.routers')), 
    path('api/' , include('apps.Users.Control_Medicos.api.routers')),
    path('api/' , include('apps.Inventarios.Control_Vacunacion.api.routers')),
    path('api/' , include('apps.Inventarios.Control_Desparasitacion.api.routers')),
    #views
    path('api/' , include('apps.Ganado.Control_Peso.api.urls')),
    path('api/' , include('apps.Ganado.Control_Empadre.api.urls')),
]

