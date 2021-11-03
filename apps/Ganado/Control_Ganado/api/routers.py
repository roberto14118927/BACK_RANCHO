from rest_framework.routers import DefaultRouter
from apps.Ganado.Control_Ganado.api.viewsets.ganado_viewsets import GanadoViewSet, GanadoListViewSet
from apps.Ganado.Control_Ganado.api.viewsets.raza_viewsets import RazaListViewSet, RazaViewSet


router = DefaultRouter()
router.register(r'ganado' , GanadoViewSet , basename='Ganado')
router.register(r'list-ganado' , GanadoListViewSet , basename='lista Ganado')
router.register(r'raza' , RazaViewSet , basename='Razas')
router.register(r'list-raza' , RazaListViewSet , basename="lista raza")

urlpatterns = router.urls