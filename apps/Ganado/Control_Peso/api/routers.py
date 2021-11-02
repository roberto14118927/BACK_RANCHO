from rest_framework.routers import DefaultRouter
from apps.Ganado.Control_Peso.api.viewsets.peso_viewsets import PesoViewSet ,PesoListViewSet 
from apps.Ganado.Control_Peso.api.viewsets.enfermedades_viewsets import EnfermedadesListViewSet ,EnfermedadesViewSet
from apps.Ganado.Control_Peso.api.viewsets.asociadas_viewset import AsociadasListViewSet ,AsociadasViewSet


router = DefaultRouter()
router.register(r'pesos' , PesoViewSet , basename='Peso')
router.register(r'list-pesos' , PesoListViewSet , basename='lista de pesos')

router.register(r'enfermedades' , EnfermedadesViewSet , basename='Peso')
router.register(r'list-enfermedades' , EnfermedadesListViewSet , basename='lista de pesos')

router.register(r'asociadas' , AsociadasViewSet , basename='Peso')
router.register(r'list-asociadas' , AsociadasListViewSet , basename='lista de pesos')

urlpatterns = router.urls