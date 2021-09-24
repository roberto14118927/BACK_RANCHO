from Control_G import serializer
from Control_G.models import Ganado
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

from Control_P.models import Peso_Ganando , Enfermedades_Ganado , Vacas_asociadas
from Control_P.serializer import Create_enfermedad, Peso_Serializer , Vacas_Serializer , Enfermedades_Serializer


#------------ VIEWS PARA EL PESO DEL GANADO ---------------------------
#TRAE TODOS LOS pesos
class Peso_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Peso_Ganando.objects.all().order_by("id")
            serializer = Peso_Serializer(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except: 
            return Response(status = status.HTTP_400_BAD_REQUEST)


#TRAE EL PESO DEL GANADO POR ID
class PesoList_By_Id(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Peso_Ganando.objects.all().filter(id=id)
                if len(queryset) > 0: 
                    serializer = Peso_Serializer(queryset, many= True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO PESO DE GANADO
class Peso_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        print("Datos: " , request.data)
        id = request.data["id_ganado"]
        try:
            topic = Ganado.objects.get(id=id)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

        cow_data = request.data
        cow_data["id_ganado"] = topic

        new_cow = Peso_Ganando.objects.create(
            id_ganado = cow_data["id_ganado"],
            dia_peso = cow_data["dia_peso"],
            mes_peso = cow_data["mes_peso"],
            anio_peso = cow_data["anio_peso"],
            ganancia_peso_mensual_kilo = cow_data["ganancia_peso_mensual_kilo"],
            ganancia_peso_mensual_porcentaje = cow_data["ganancia_peso_mensual_porcentaje"],
            estado_vaca = cow_data["estado_vaca"],
            peso = cow_data["peso"]
        )

        new_cow.save()
        serializer = Peso_Serializer(new_cow)

        return Response(serializer.data , status=status.HTTP_201_CREATED)


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
            queryset = Enfermedades_Ganado.objects.all().order_by("id")
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
                queryset = Enfermedades_Ganado.objects.all().filter(id=id)
                if len(queryset) > 0: 
                    serializer = Enfermedades_Serializer(queryset, many= True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA NUEVA ENFERMDAD
class Enfermedad_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = Create_enfermedad(data = request.data)
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
            queryset = Vacas_asociadas.objects.all().order_by("id")
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
                queryset = Vacas_asociadas.objects.all().filter(id=id)
                if len(queryset) > 0: 
                    serializer = Vacas_Serializer(queryset , many=True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA NUEVA ASOCIACIÓN
class Asociacion_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        print("Datos: " , request.data)

        id_ganado = request.data["id_ganado"]
        id_enfermedad = request.data["id_enfermedad"]
        try:
            topic_g = Ganado.objects.get(id=id_ganado)
            topic_e = Enfermedades_Ganado.objects.get(id=id_enfermedad)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

        cow_data = request.data
        cow_data["id_ganado"] = topic_g
        cow_data["id_enfermedad"] = topic_e

        new_cow = Vacas_asociadas.objects.create(
            id_ganado = cow_data["id_ganado"],
            id_enfermedad = cow_data["id_enfermedad"]
        )

        new_cow.save()
        serializer = Vacas_Serializer(new_cow)

        return Response(serializer.data , status=status.HTTP_201_CREATED)



#ACTUALIZA UNA ASOCIACIÓN
class Asociacion_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Vacas_asociadas.objects.get(id = id)
            print("dato: " , request.data)
            serializer = Vacas_Serializer(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)
        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UNa ASOCIACIÓN 
class Asociacion_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Vacas_asociadas.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)