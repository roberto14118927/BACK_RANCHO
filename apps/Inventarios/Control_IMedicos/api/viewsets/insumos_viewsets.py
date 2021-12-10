from rest_framework.response import Response
from rest_framework import status , viewsets

from apps.Users.Control_Login.api.authentication_mixed import Authentication
from apps.Inventarios.Control_IMedicos.api.serializers.insumos_serializers import InventarioInsumosSerializer


#agregar el Authentication como primer parametro.
class InsumosViewSet(Authentication ,viewsets.ModelViewSet):
    serializer_class = InventarioInsumosSerializer
    queryset = serializer_class().Meta.model.objects.filter()

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    # def update(self , request , pk=None):
    #     serialize = self.serializer_class(self.get_queryset(pk), data = request.data)
    #     if serialize.is_valid():
    #         serialize.save()
    #         return Response(data = serialize.data , status= status.HTTP_200_OK)
    #     return Response({'message': 'No encontrado put'} , status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self , request , pk=None):
        serializer = self.get_queryset().filter(id=pk).first()
        if serializer:
            serializer.delete()
            return Response({'message': 'Eliminado'} , status= status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)