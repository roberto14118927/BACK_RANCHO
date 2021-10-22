from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status


from Control_IA.models import Inventario_Alimentos
from Control_IA.serializer import InventarioAlimentos_Serializer

# Create your views here.

class InventarioAlimentos_List(APIView):
    def get (self , request ):
        try:
            queryset = Inventario_Alimentos.objects.all().order_by("id")
            serializer = InventarioAlimentos_Serializer(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response( status = status.HTTP_400_BAD_REQUEST)

class InventarioAlimentos_byID(APIView):
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Inventario_Alimentos.objects.filter(id=id)
                if len(queryset) > 0: 
                    serializer = InventarioAlimentos_Serializer(queryset , many=True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)


class InventarioAlimentos_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = InventarioAlimentos_Serializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response( status = status.HTTP_400_BAD_REQUEST)


#ACTUALIZA UN MEDICO
class InventarioAlimentos_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Inventario_Alimentos.objects.get(id = id)
            serializer = InventarioAlimentos_Serializer(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response( status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN MEDICO 
class InventarioAlimentos_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Inventario_Alimentos.objects.get(id=id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)


