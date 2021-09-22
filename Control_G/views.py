from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator

from Control_G.serializer import RazaSerializers , GanadoSerializers
from Control_G.models import Raza , Ganado


#----------- VIEWS PARA RAZA ----------------------------
#TRAE TODAS LAS RAZAS REGISTRADAS
class RazaList(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Raza.objects.all()
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
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


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
            queryset = Ganado.objects.all()
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
                queryset = list(Ganado.objects.filter(id=id).values())
                if len(queryset) > 0: 
                    cows = queryset[0]
                    return Response(cows , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO GANADO
class GanadoCreate(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = GanadoSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

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