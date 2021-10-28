from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from apps.Users.Control_Login.views import Login , Logout , UserToken

schema_view = get_swagger_view(title='Pastebin API')
router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('documentacion', schema_view),

    path('login/' , Login.as_view()),
    path('logout/', Logout.as_view()),
    path('refresh-token/' , UserToken.as_view()),

    path('usuario/', include("apps.Users.Control_Usuario.api.routers")),
    path('api/' , include('apps.Ganado.Control_Ganado.api.routers')),
]




# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('documentacion', schema_view),

#     #control de ganado
#     path(r'api/cows/' , include('apps.Ganado.Control_Ganado.urls')),
#     path(r'api/peso/' , include('apps.Ganado.Control_Peso.urls')),
#     path(r'api/empadre/' , include('apps.Ganado.Control_Empadre.urls')),

#     #Control de inventarios
#     path(r'api/termocrio/', include('apps.Inventarios.Control_Termo.urls')),
#     path(r'api/inv/' , include('apps.Inventarios.Control_IAlimentos.urls')),
#     path(r'api/inv/' , include('apps.Inventarios.Control_IMedicos.urls')),
#     path(r'api/inv/' , include('apps.Inventarios.Control_IMateriales.urls')),

#     #Control de usuarios
#     path(r'api/medicos/', include('apps.Users.Control_Medicos.urls')),
#     path(r'usuario/', include("apps.Users.Control_Usuario.api.urls"))
    
#     #Login
# ]
