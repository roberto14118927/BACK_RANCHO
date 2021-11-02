
from rest_framework.routers import DefaultRouter
from apps.Users.Control_Medicos.api.viewsets.medico_viewsets import MedicoEspViewSet
from apps.Users.Control_Medicos.api.viewsets.empadre_viewsets import EmpadreViewSet, EmpadreListViewSet


router = DefaultRouter()
router.register(r'medicos' , MedicoEspViewSet , basename='Medicos')
router.register(r'empadre-medicos' , EmpadreViewSet , basename='Empadre medicos')
router.register(r'list-empadre-medicos' , EmpadreListViewSet , basename='Lista empadre medicos')

urlpatterns = router.urls