from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from apps.Users.Control_Login.api.authentication_mixed import Authentication
from apps.Ganado.Control_Empadre.api.serializers.tacto_serializers import TactoSerializers
from apps.Ganado.Control_Empadre.models import  Tacto


#----------------VIEWS PARA TACTO ----------------------
#TRAE LAS ASOCIACIONES POR ID de empadre
class Tacto_by_id_empadre(Authentication , APIView):
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Tacto.objects.filter(id_empadre=id)
                if len(queryset) > 0: 
                    serializer = TactoSerializers(queryset , many=True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
