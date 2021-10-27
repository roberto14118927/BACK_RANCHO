from django.db.models import base
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter, SimpleRouter
from apps.Ganado.Control_Ganado.api.views.ganado_views import GanadoViewSet 

router = DefaultRouter()
router.register(r'ganado' , GanadoViewSet , basename='Ganado')

urlpatterns = router.urls