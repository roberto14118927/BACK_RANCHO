
from rest_framework.routers import DefaultRouter
from apps.Users.Control_Usuario.api.viewsets import UsuarioCreateViewSet , UsuarioViewSet


router = DefaultRouter()
router.register(r'users' , UsuarioViewSet , basename='Usuarios')
router.register(r'create-user' , UsuarioCreateViewSet , basename='Create users')

urlpatterns = router.urls