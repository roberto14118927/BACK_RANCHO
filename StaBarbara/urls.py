from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/user/', include('Social.urls')),
    path(r'api/auth/', include('Login.urls')),
    path(r'api/cows/' , include('Control_G.urls')),
    path(r'api/peso/' , include('Control_P.urls')),
    path(r'api/empadre/' , include('Control_Em.urls')),
    path(r'api/termocrio/', include('Control_T.urls')),
    path(r'api/medicos/', include('Control_M.urls')),
    path(r'api/inv/' , include('Control_IA.urls')),
    path(r'api/inv/' , include('Control_IM.urls')),
    path(r'api/inv/' , include('Control_IMA.urls')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #re_path(r'^',include(router.urls)),
    path('documentacion', schema_view),
]
