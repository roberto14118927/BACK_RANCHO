from rest_framework.response import Response
from rest_framework import status , viewsets

from apps.Users.Control_Login.api.authentication_mixed import Authentication
from apps.Ganado.Control_Ganado.api.serializers.raza_serializers import RazaSerializer


class RazaListViewSet(viewsets.ModelViewSet):
    serializer_class = RazaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter().order_by("id")
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        peso = self.get_serializer(self.get_queryset(), many=True)
        return Response(peso.data, status=status.HTTP_200_OK)


class RazaViewSet(viewsets.ModelViewSet):
    serializer_class = RazaSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter().order_by("id")
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
  
    def list(self, request):
        ganado = self.get_serializer(self.get_queryset(), many=True)
        return Response(ganado.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
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


