from rest_framework.response import Response
from rest_framework import status, viewsets

from apps.Users.Control_Login.api.authentication_mixed import Authentication
from apps.Inventarios.Control_Termocrio.api.serializers.empadre_serializers import EmpadreTermoListSerializers, EmpadreTermoSerializers

class EmpadreListViewSet(viewsets.ModelViewSet):
    serializer_class = EmpadreTermoListSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        empadre = self.get_serializer(self.get_queryset(), many=True)
        return Response(empadre.data, status=status.HTTP_200_OK)


#agregar el Authentication como primer parametro.
class EmpadreViewSet(viewsets.ModelViewSet):
    serializer_class = EmpadreTermoSerializers
    queryset = serializer_class().Meta.model.objects.filter()

    def get_queryset(self , pk = None):
        if pk is None:
            return self.serializer_class().Meta.model.objects.filter().order_by("id")
        return self.serializer_class().Meta.model.objects.filter().first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Creado correctamente'} , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def update(self , request , pk=None):
        serialize = self.serializer_class(self.get_queryset(pk), data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data = serialize.data , status= status.HTTP_200_OK)
        return Response({'message': 'No encontrado put'} , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk=None):
        cow = self.get_queryset().filter(id=pk).first()
        if cow:
            cow.delete()
            return Response({'message': 'Eliminado'} , status= status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)