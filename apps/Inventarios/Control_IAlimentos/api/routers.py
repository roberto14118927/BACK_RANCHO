from rest_framework.routers import DefaultRouter

from apps.Inventarios.Control_IAlimentos.api.viewsets.alimento_viewsets import AlimentoViewSet


router = DefaultRouter()
router.register(r'inventario-alimentos' , AlimentoViewSet , basename='Inventario alimentos')
urlpatterns = router.urls