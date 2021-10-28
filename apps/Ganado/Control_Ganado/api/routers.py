from django.db.models import base
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from apps.Ganado.Control_Ganado.api.viewsets.ganado_viewsets import GanadoViewSet, GanadoListViewSet
from apps.Ganado.Control_Ganado.api.viewsets.raza_viewsets import RazaViewSet


router = DefaultRouter()
router.register(r'ganado' , GanadoViewSet , basename='Ganado')
router.register(r'list-ganado' , GanadoListViewSet , basename='Ganado')

router.register(r'raza' , RazaViewSet , basename='Razas')

urlpatterns = router.urls