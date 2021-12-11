from rest_framework.response import Response
from rest_framework import status, viewsets

from apps.Users.Control_Login.api.authentication_mixed import Authentication
from apps.Inventarios.Control_Vacunacion.api.serializers.vacuna_serializers import VacunaSerializers , VacunaListSerializers
from rest_framework.decorators import action
import django_excel as excel
from pyexcel_xlsx import save_data
from collections import OrderedDict
from datetime import datetime
import json



class VacunaListViewSet(viewsets.ModelViewSet):
    serializer_class = VacunaListSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        empadre = self.get_serializer(self.get_queryset(), many=True)
        return Response(empadre.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], name='excel')
    def excel(self, request, *args, **kwargs):
        vacunaciones = self.get_serializer(self.get_queryset(), many=True)

        export = [] 
        export.append(['Nombre', 'Medicamento','Fecha de vacunación'])
        # dict_items = vacunaciones.data.items()
        for value in vacunaciones.data:
            # print(value)
            lista = json.dumps(list(value.items()))
            # print(lista)
            data = json.loads(lista)
            # print(data)
            # print(type(data))
            # print(type(data[1]))
            # print(type(data[2]))
            # print(data[1][1])
            medicamento = json.dumps(data[1][1])
            medicamentoJson = json.loads(medicamento)
            vacaAux = json.dumps(data[2][1])
            vaca = json.loads(vacaAux)
            export.append([vaca.get("nombre"), medicamentoJson.get("nombre"), data[3][1]])
            
           
        # Transcribir la data a una hoja de calculo en memoria
        sheet = excel.pe.Sheet(export)
        #save_data("your_file.xlsx", export)

        # Generar el archivo desde la hoja en memoria con 
        # un nombre de archivo que recibirás en el navegador
        return excel.make_response(sheet, "xlsx", file_name="results.xlsx")

        


#agregar el Authentication como primer parametro.
class VacunaViewSet(viewsets.ModelViewSet):
    serializer_class = VacunaSerializers
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
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk=None):
        cow = self.get_queryset().filter(id=pk).first()
        if cow:
            cow.delete()
            return Response({'message': 'Eliminado'} , status= status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)