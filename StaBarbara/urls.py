"""StaBarbara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import Control_P
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url 
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
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
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #re_path(r'^',include(router.urls)),
    path('documentacion', schema_view),
]
