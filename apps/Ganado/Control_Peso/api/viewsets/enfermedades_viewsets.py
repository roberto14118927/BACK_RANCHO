from rest_framework.response import Response
from rest_framework import status , viewsets

from apps.Ganado.Control_Peso.models import Peso_Ganando
from apps.Users.Control_Login.api.authentication_mixed import Authentication
from apps.Ganado.Control_Peso.api.serializers.enfermedades_serializers import EnfermedadesListSerializer , EnfermedadesSerializer


class EnfermedadesListViewSet(Authentication ,viewsets.ModelViewSet):
    serializer_class = EnfermedadesListSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        peso = self.get_serializer(self.get_queryset(), many=True)
        return Response(peso.data, status=status.HTTP_200_OK)


class EnfermedadesViewSet(Authentication ,viewsets.ModelViewSet):
    serializer_class = EnfermedadesSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        peso = self.get_serializer(self.get_queryset(), many=True)
        return Response(peso.data, status=status.HTTP_200_OK)

    def create(self, request):
        # send information to serializer
        serializer = self.serializer_class(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            peso = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if peso.is_valid():
                peso.save()
                return Response(peso.data, status=status.HTTP_200_OK)
            return Response(peso.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        peso = self.get_queryset().filter(id=pk).first() # get instance        
        if peso:
            peso.delete()
            return Response({'message':'Eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe!'}, status=status.HTTP_400_BAD_REQUEST)