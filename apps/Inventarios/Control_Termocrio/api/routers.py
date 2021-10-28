from rest_framework.routers import DefaultRouter
from apps.Inventarios.Control_Termocrio.api.viewsets.termo_viewsets import  TermoViewSet , TermoListViewSet
from apps.Inventarios.Control_Termocrio.api.viewsets.empadre_serializers import EmpadreListViewSet, EmpadreViewSet

router = DefaultRouter()
router.register(r'inventario-termo' , TermoViewSet , basename='Inventario termo')
router.register(r'inventario-list-termo' , TermoListViewSet , basename='lista termo')

router.register(r'empadre-termo' , EmpadreViewSet , basename='Empadre termo')
router.register(r'list-empadre-termo' , EmpadreListViewSet , basename='Lista empadre termo')

urlpatterns = router.urls