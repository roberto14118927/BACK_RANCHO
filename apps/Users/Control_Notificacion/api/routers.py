from rest_framework.routers import DefaultRouter
from apps.Users.Control_Notificacion.api.viewsets.notificacion_viewsets import NotiViewSet , NotiListViewSet


router = DefaultRouter()
router.register(r'control-notificacion' , NotiViewSet , basename='Notificaciones')
router.register(r'notificacion-list' , NotiListViewSet , basename='lista notificaciones')

urlpatterns = router.urls