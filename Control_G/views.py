from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from django.utils.decorators import method_decorator

from Control_G.serializer import RazaSerializers , GanadoSerializers
from Control_G.models import Raza , Ganado


#----------- VIEWS PARA RAZA ----------------------------
#TRAE TODAS LAS RAZAS REGISTRADAS
class RazaList(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Raza.objects.all().order_by("id")
            serializer = RazaSerializers(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#TRAE UNA RAZA POR ID
class RazaListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = list(Raza.objects.filter(id=id).values())
                if len(queryset) > 0: 
                    cows = queryset[0]
                    return Response(cows , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                
#CREA UNA NUEVA RAZA DE GANADO
class RazaCreate(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = RazaSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)


#ACTUALIZA UN GANADO
class RazaUpdate(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Raza.objects.get(id = id)
            serializer = RazaSerializers(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN GANADO 
class RazaDelete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Raza.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)


#------------ VIEWS PARA GANADO ---------------------------
#TRAE TODOS LOS USUARIOS
class GanadoList(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Ganado.objects.all().order_by("id")
            serializer = GanadoSerializers(queryset, many= True)
           
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#TRAE GANADO POR ID
class GanadoListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Ganado.objects.all().filter(id=id)
                if len(queryset) > 0: 
                    serializer = GanadoSerializers(queryset, many= True)
                    return Response(data= serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

class GanadoCreate(APIView):
    @method_decorator(csrf_exempt)
    def post(self , request):

        id = request.data["id_raza"] 
        try:
            topic = Raza.objects.get(id = id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        cow_data = request.data
        cow_data["id_raza"] = topic
        new_cow = Ganado.objects.create(
            nombre = cow_data["nombre"],
            sexo = cow_data["sexo"],
            id_raza = cow_data["id_raza"], 
            num_economico = cow_data["num_economico"] ,
            num_registro = cow_data ["num_registro"],
            num_siniga =  cow_data["num_siniga"],
            comentarios = cow_data["comentarios"],
            fecha_nacimiento = cow_data["fecha_nacimiento"],
            padre = cow_data ["padre"],
            madre = cow_data["madre"] ,
            fecha_entrada_hato  = cow_data ["fecha_entrada_hato"],
            estado  = cow_data ["estado"],
            condicion_estadia  = cow_data ["condicion_estadia"]
        )

        new_cow.save()
        serializer = GanadoSerializers(new_cow)

        return Response(serializer.data)


#ACTUALIZA UN GANADO
class GanadoUpdate(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Ganado.objects.get(id = id)
            serializer = GanadoSerializers(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN GANADO 
class GanadoDelete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Ganado.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)