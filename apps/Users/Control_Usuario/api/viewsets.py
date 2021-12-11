from rest_framework.response import Response
from rest_framework import status, viewsets

from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from apps.Users.Control_Usuario.api.serializer import (
 UserSerializer , UserListSerializer ,  UpdateUserSerializer , PasswordSerializer)
from apps.Users.Control_Login.api.authentication_mixed import Authentication

class CreateViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer

    #Crear usuarios
    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(data = user_serializer.data , status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class UsuarioViewSet(Authentication,  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None

    def get_object(self , pk):
        return get_object_or_404(self.serializer_class.Meta.model , pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class().Meta.model.objects.filter()
        return self.queryset


    #Actualizar contraseña
    @action(detail=True, methods=['POST'])
    def set_password(self , request, pk=None):
        user = self.get_object(pk)

        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response(
                {'message:' : 'Contraseña actualizada correctamente.'}, 
                status=status.HTTP_200_OK )
        return Response({
                'message:' : 'Error al actualizar.' , 
                'errors': password_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST )

    #listar usuarios
    def list(self, request):
        users = self.get_queryset()
        user_serialiazer = self.list_serializer_class(users, many=True)
        return Response(user_serialiazer.data , status=status.HTTP_200_OK)


    #Listar usuarios por id
    def retrieve(self , request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data , status=status.HTTP_200_OK)
    
    #Actualizar usuarios
    def update(self , request , pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data , status=status.HTTP_201_CREATED)
        return Response({'message:' : 'Error al actualizar.' , 'errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST )

    #Eliminar usuarios
    def destroy(self, request, pk=None):
        user = self.get_queryset().filter(id=pk).first() # get instance        
        if user:
            user.delete()
            return Response({'message':'Eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe!'}, status=status.HTTP_400_BAD_REQUEST)
