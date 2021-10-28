from rest_framework.routers import DefaultRouter

from apps.Inventarios.Control_IMedicos.api.viewsets.insumos_viewsets import InsumosViewSet


router = DefaultRouter()
router.register(r'inventario-insumos' , InsumosViewSet , basename='Inventario alimentos')
urlpatterns = router.urls