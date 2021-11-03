from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from apps.Users.Control_Login.api.authentication_mixed import Authentication

from apps.Ganado.Control_Peso.models import Peso_Ganando , Vacas_asociadas
from apps.Ganado.Control_Peso.api.serializers.peso_serializers import PesoSerializer
from apps.Ganado.Control_Peso.api.serializers.asociadas_serializers import AsociadasSerializer

#------------ VIEWS PARA EL PESO DEL GANADO ---------------------------
#TRAE EL PESO DEL GANADO POR ID
class PesoList_By_IdGanado(Authentication , APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Peso_Ganando.objects.filter(id_ganado=id)
                if len(queryset) > 0: 
                    serializer = PesoSerializer(queryset, many= True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)


#TRAE LAS ASOCIACIONES POR ID
class Asociaciones_List_By_enfermedad(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Vacas_asociadas.objects.all().filter(id_enfermedad=id)
                if len(queryset) > 0: 
                    serializer = AsociadasSerializer(queryset , many=True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
