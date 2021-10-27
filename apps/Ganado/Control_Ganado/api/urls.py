from django.urls import path
from apps.Ganado.Control_Ganado.api.views.raza_views import RazaListAPIView
from apps.Ganado.Control_Ganado.api.views.ganado_views import (
    GanadoListAPIView, CreateGanadoAPIView, GanadoRetrieveAPIView , GanadoDestroyAPIView, GanadoUpdateAPIView)

from apps.Ganado.Control_Ganado.api.views.raza_views import (
    RazaCreateAPIView , RazaListAPIView , RazaDestroyAPIView , RazaUpdateAPIView , RazaRetrieveAPIView)

urlpatterns = [
    path('ganado/list/' , GanadoListAPIView.as_view()),
    path('ganado/create/', CreateGanadoAPIView.as_view()),
    path('ganado/id/<int:pk>/', GanadoRetrieveAPIView.as_view()),
    path('ganado/delete/<int:pk>/', GanadoDestroyAPIView.as_view()),
    path('ganado/update/<int:pk>/', GanadoUpdateAPIView.as_view()),


    path('raza/list/' , RazaListAPIView.as_view() , name='Razas'),
    path('raza/create/' , RazaCreateAPIView.as_view()),
    path('raza/id/<int:pk>' , RazaRetrieveAPIView.as_view()),
    path('raza/delete/<int:pk>' , RazaDestroyAPIView.as_view()),
    path('raza/update/<int:pk>', RazaUpdateAPIView.as_view())
]