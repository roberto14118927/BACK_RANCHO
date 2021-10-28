from django.db.models import base
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from apps.Ganado.Control_Empadre.api.viewsets.empadre_viewsets import EmpadreViewSet , EmpadreListViewSet
from apps.Ganado.Control_Empadre.api.viewsets.tacto_viewsets import TactoListViewSet , TactoViewSet


router = DefaultRouter()
router.register(r'empadre' , EmpadreViewSet , basename='Empadre')
router.register(r'list-empadre' , EmpadreListViewSet , basename='Lista empadres')

router.register(r'tacto' , TactoViewSet , basename='Tactos')
router.register(r'list-tacto' , TactoViewSet , basename='Lista tactos')

urlpatterns = router.urls