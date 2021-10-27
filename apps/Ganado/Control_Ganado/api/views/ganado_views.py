from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets

from apps.base.api import GeneralListApiView
from apps.Ganado.Control_Ganado.models import Ganado
from apps.Ganado.Control_Ganado.api.serializers.ganado_serializers import GanadoSerializer , GanadoListSerializer


class GanadoViewSet(viewsets.ModelViewSet):
    serializer_class = GanadoSerializer
    queryset =  GanadoSerializer.Meta.model.objects.filter(state=True)
  
    def get_queryset(self , pk = None):
        if pk is None:
            return GanadoListSerializer().Meta.model.objects.filter(state = True)
        return GanadoListSerializer().Meta.model.objects.filter(state = True).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Creado correctamente'} , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
  
    def list(self , request):
        queryset = Ganado.objects.all().order_by("id")
        serializer = GanadoListSerializer(queryset, many= True)
        return Response(data = serializer.data , status= status.HTTP_200_OK)

    def update(self, request , pk=None):
        if self.get_queryset(pk):
            serialize = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(data = serialize.data , status= status.HTTP_200_OK)
            return Response({'message': 'No encontrado put'} , status=status.HTTP_400_BAD_REQUEST)      

    def delete(self, request ,  pk=None):
        cow = self.get_queryset().filter(id=pk).first()
        if cow:
            cow.state = False
            cow.save()
            return Response({'message': 'Eliminado'} , status= status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)


