from django.urls import path
from apps.Users.Control_Usuario.api.api import user_api_view , user_detail_view

urlpatterns = [
    path('list/', user_api_view , name="Usuario_api" ),
    path('list/<int:pk>/', user_detail_view , name="by id")
]