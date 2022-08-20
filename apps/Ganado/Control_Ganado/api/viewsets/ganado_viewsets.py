from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


from apps.Ganado.Control_Ganado.models import Ganado
from apps.Users.Control_Login.api.authentication_mixed import Authentication
from apps.Ganado.Control_Ganado.api.serializers.ganado_serializers import GanadoSerializer , GanadoListSerializer

from rest_framework.decorators import action
import django_excel as excel
from pyexcel_xlsx import save_data
from collections import OrderedDict
from datetime import datetime
import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class GanadoListViewSet(viewsets.ModelViewSet): # agregar autenticacion
    queryset = Ganado.objects.all()
    serializer_class = GanadoListSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['num_registro']


    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        peso = self.get_serializer(queryset, many=True)
        return Response(peso.data, status=status.HTTP_200_OK)

    
    @action(detail=False, methods=['GET'], name='excel')
    def excel(self, request, *args, **kwargs):
        ganado = self.get_serializer(self.get_queryset(), many=True)
        export = [] 
        export.append(['Inventario de ganado'])
        export.append(['Nombre', 'Sexo','Raza','N.Económico','N.Registro','N.Siniga','Fecha de nacimiento','Fecha de entrada al hato','estado','Condicion Estadia'])
        # dict_items = ganado.data.items()
        for value in ganado.data:
            # print(value)
            lista = json.dumps(list(value.items()))
            # print(lista)
            data = json.loads(lista)
            razaAux = json.dumps(data[13][1])
            raza = json.loads(razaAux)
            sexoAux = json.dumps(data[2][1])
            sexo = json.loads(sexoAux)
            export.append([data[1][1], data[2][1], raza.get("raza"),data[3][1], data[4][1],
            data[5][1],data[7][1],data[10][1], data[11][1], data[12][1]])
            
           
        # Transcribir la data a una hoja de calculo en memoria
        sheet = excel.pe.Sheet(export)
        #save_data("your_file.xlsx", export)

        # Generar el archivo desde la hoja en memoria con 
        # un nombre de archivo que recibirás en el navegador
        return excel.make_response(sheet, "xlsx", file_name="results.xlsx")


#Agregar el Authentication
class GanadoViewSet(Authentication ,viewsets.ModelViewSet):
    serializer_class = GanadoSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                            serializer.data,
                            status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        ganado = GanadoListSerializer(self.get_queryset(), many=True)
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


