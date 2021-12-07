
from rest_framework.routers import DefaultRouter
from apps.Users.Control_Usuario.api.viewsets import  UsuarioViewSet, CreateViewSet


router = DefaultRouter()
router.register(r'users' , UsuarioViewSet , basename='Usuarios')
router.register(r'create-user' , CreateViewSet , basename='Create users')

urlpatterns = router.urls