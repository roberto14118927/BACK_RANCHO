from rest_framework.routers import DefaultRouter
from apps.Inventarios.Control_Desparasitacion.api.viewsets.desp_viewsets import DespListViewSet , DespViewSet


router = DefaultRouter()
router.register(r'control-desp' , DespViewSet , basename='Desparasitacion')
router.register(r'desp-list' , DespListViewSet , basename='lista Desparasitacion')

urlpatterns = router.urls