from django.db.models import base
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from apps.Ganado.Control_Ganado.api.views.ganado_views import GanadoViewSet 
from apps.Ganado.Control_Ganado.api.views.raza_views import RazaViewSet


router = DefaultRouter()
router.register(r'ganado' , GanadoViewSet , basename='Ganado')
router.register(r'raza' , RazaViewSet , basename='Razas')

urlpatterns = router.urls