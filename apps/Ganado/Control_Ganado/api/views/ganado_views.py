from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


from apps.Ganado.Control_Ganado.models import Ganado
from apps.Users.Control_Login.api.authentication_mixed import Authentication
from apps.Ganado.Control_Ganado.api.serializers.ganado_serializers import GanadoSerializer , GanadoListSerializer


class GanadoListViewSet(Authentication,  viewsets.ModelViewSet):
    serializer_class = GanadoListSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        peso = self.get_serializer(self.get_queryset(), many=True)
        return Response(peso.data, status=status.HTTP_200_OK)


#Agregar el Authentication
class GanadoViewSet(Authentication , viewsets.ModelViewSet):
    serializer_class = GanadoSerializer
    
    def get_queryset(self, pk=None):
        pass

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Creado correctamente'} , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
  
    def list(self, request):
        ganado = self.get_serializer(self.get_queryset(), many=True)
        return Response(ganado.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request ,  pk=None):
        cow = self.get_queryset().filter(id=pk).first()
        if cow:
            cow.delete()
            return Response({'message': 'Eliminado'} , status= status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)


