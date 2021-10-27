from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status


from apps.Inventarios.Control_IMedicos.models import Inventario_Insumos
from apps.Inventarios.Control_IMedicos.serializer import InventarioInsumos_Serializer

# Create your views here.

class InventarioInsumos_List(APIView):
    def get (self , request ):
        try:
            queryset = Inventario_Insumos.objects.all().order_by("id")
            serializer = InventarioInsumos_Serializer(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response( status = status.HTTP_400_BAD_REQUEST)

class InventarioInsumos_byID(APIView):
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Inventario_Insumos.objects.filter(id=id)
                if len(queryset) > 0: 
                    serializer = InventarioInsumos_Serializer(queryset , many=True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)


class InventarioInsumos_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = InventarioInsumos_Serializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response( status = status.HTTP_400_BAD_REQUEST)


#ACTUALIZA UN MEDICO
class InventarioInsumos_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Inventario_Insumos.objects.get(id = id)
            serializer = InventarioInsumos_Serializer(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response( status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN MEDICO 
class InventarioInsumos_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Inventario_Insumos.objects.get(id=id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)


