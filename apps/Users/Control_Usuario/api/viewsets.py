from rest_framework.response import Response
from rest_framework import status, viewsets

from apps.Users.Control_Usuario.api.serializer import  UserSerializer , UserListSerializer
from apps.Users.Control_Login.api.authentication_mixed import Authentication


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UserListSerializer
    queryset = UserListSerializer.Meta.model.objects.filter()

    def get_queryset(self , pk=None):
        if pk is None:
            return UserListSerializer().Meta.model.objects.filter().order_by("id")
        return UserListSerializer().Meta.model.objects.filter().first()

    def update(self, request, pk=None):
        serialize = UserSerializer(self.get_queryset(pk), data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data = serialize.data , status= status.HTTP_200_OK)
        return Response({'message': 'No encontrado put'} , status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk=None):
        user = UserSerializer().filter(id=pk).first()
        if user:
            user.delete()
            return Response({'message': 'Eliminado'} , status= status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)
        
        
class UsuarioCreateViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.filter(id = 0)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Creado correctamente'} , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
