from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

from Control_P.models import Peso_Ganando , Enfermedades_Ganado , Vacas_asociadas
from Control_P.serializer import Peso_Serializer , Vacas_Serializer , Enfermedades_Serializer


#------------ VIEWS PARA EL PESO DEL GANADO ---------------------------
#TRAE TODOS LOS pesos
class Peso_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Peso_Ganando.objects.all()
            serializer = Peso_Serializer(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#TRAE EL PESO DEL GANADO POR ID
class PesoList_By_Id(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = list(Peso_Ganando.objects.filter(id=id).values())
                if len(queryset) > 0: 
                    cows = queryset[0]
                    return Response(cows , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO PESO DE GANADO
class Peso_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = Peso_Serializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ACTUALIZA UN PESO DE GANADO
class Peso_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Peso_Ganando.objects.get(id = id)
            serializer = Peso_Serializer(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN PESO DE GANADO 
class Peso_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Peso_Ganando.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)


# ===================================== ENFERMEDADES GANADO ============================================#

#TRAE TODAS LOS ENFERMEDADES
class Enfermedades_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Enfermedades_Ganado.objects.all()
            serializer = Enfermedades_Serializer(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#TRAE LAS ENFERMEDADES POR ID
class Enfermedades_List_By_Id(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = list(Enfermedades_Ganado.objects.filter(id=id).values())
                if len(queryset) > 0: 
                    cows = queryset[0]
                    return Response(cows , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA NUEVA ENFERMDAD
class Enfermedad_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = Enfermedades_Ganado(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ACTUALIZA UNA ENFERMEDAD
class Enfermedad_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Enfermedades_Ganado.objects.get(id = id)
            serializer = Enfermedades_Serializer(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN PESO DE GANADO 
class Enfermedad_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Enfermedades_Ganado.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)



# ==================================================== VACAS ASOCIADAS =======================
#TRAE TODAS LAS ASOCIACIONES
class Asociation_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Vacas_asociadas.objects.all()
            serializer = Vacas_Serializer(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#TRAE LAS ASOCIACIONES POR ID
class Asociaciones_List_By_Id(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = list(Vacas_asociadas.objects.filter(id=id).values())
                if len(queryset) > 0: 
                    cows = queryset[0]
                    return Response(cows , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA NUEVA ASOCIACIÓN
class Asociacion_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = Vacas_asociadas(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
