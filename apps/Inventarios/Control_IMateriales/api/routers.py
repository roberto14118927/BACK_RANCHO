from rest_framework.routers import DefaultRouter

from apps.Inventarios.Control_IMateriales.api.viewsets.materiales_viewsets import MaterialesViewSet


router = DefaultRouter()
router.register(r'inventario-materiales' , MaterialesViewSet , basename='Inventario alimentos')
urlpatterns = router.urls