from django.urls import path, re_path
from django.contrib.auth.models import User
from Login import views

from Login import views 

urlpatterns = [
    re_path(r'login/$', views.CustonAuthToken.as_view()),
]