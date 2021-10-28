from django.urls import path
from apps.Ganado.Control_Ganado.api.views.raza_views import RazaListAPIView
from apps.Ganado.Control_Ganado.api.views.raza_views import (
    RazaCreateAPIView , RazaListAPIView , RazaDestroyAPIView , RazaUpdateAPIView , RazaRetrieveAPIView)

urlpatterns = [

    path('raza/list/' , RazaListAPIView.as_view() , name='Razas'),
    path('raza/create/' , RazaCreateAPIView.as_view()),
    path('raza/id/<int:pk>' , RazaRetrieveAPIView.as_view()),
    path('raza/delete/<int:pk>' , RazaDestroyAPIView.as_view()),
    path('raza/update/<int:pk>', RazaUpdateAPIView.as_view())
]