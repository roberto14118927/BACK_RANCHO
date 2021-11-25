from rest_framework.routers import DefaultRouter
from apps.Inventarios.Control_Vacunacion.api.viewsets.vacuna_viewsets import VacunaListViewSet , VacunaViewSet


router = DefaultRouter()
router.register(r'control-vacunas' , VacunaViewSet , basename='Vacunas')
router.register(r'vacunas-list' , VacunaListViewSet , basename='lista vacunas')

urlpatterns = router.urls

