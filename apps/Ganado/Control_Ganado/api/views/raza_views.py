from apps.base.api import GeneralListApiView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.Ganado.Control_Ganado.api.serializers.raza_serializers import RazaSerializer


class RazaListAPIView(GeneralListApiView):
    serializer_class = RazaSerializer


class RazaCreateAPIView(generics.CreateAPIView):
    serializer_class = RazaSerializer

    def post(self , request):
        print(request.data)

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Creado correctamente'} , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class RazaRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = RazaSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

class RazaDestroyAPIView(generics.DestroyAPIView):
    serializer_class = RazaSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def delete(self, request ,  pk=None):
        cow = self.get_queryset().filter(id=pk).first()
        if cow:
            cow.state = False
            cow.save()
            return Response({'message': 'Eliminado'} , status= status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)

class RazaUpdateAPIView(generics.UpdateAPIView):
    serializer_class = RazaSerializer

    def get_queryset(self , pk):
        return self.get_serializer().Meta.model.objects.filter(state=True).filter(id = pk).first()
    
    def patch(self, request , pk):
        if self.get_queryset():
            serialize = self.serializer_class(self.get_queryset(pk))
            return Response(data = serialize.data , status= status.HTTP_200_OK)
        return Response({'message': 'No encontrado patch'} , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        serialize = self.serializer_class(self.get_queryset(pk), data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data = serialize.data , status= status.HTTP_200_OK)
        return Response({'message': 'No encontrado put'} , status=status.HTTP_400_BAD_REQUEST)

    