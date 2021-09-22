from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.utils.decorators import method_decorator


from Control_E.serializer import Tacto_Serializers , Empadre_Serializers
from Control_E.models import Control_Empadre , Tacto


#------------ VIEWS PARA EMPADRE ------------------
#TRAE TODOS LOS EMPADRES
class Empadre_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Control_Empadre.objects.all()
            serializer = Empadre_Serializers(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#TRAE EMPADRE POR ID
class Empadre_ListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = list(Control_Empadre.objects.filter(id=id).values())
                if len(queryset) > 0: 
                    cows = queryset[0]
                    return Response(cows , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO EMPADRE
class Empadre_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = Empadre_Serializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ACTUALIZA UN EMPADRE
class Empadre_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Control_Empadre.objects.get(id = id)
            serializer = Empadre_Serializers(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN EMPADRE 
class Empadre_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Control_Empadre.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)


#----------------VIEWS PARA TACTO ----------------------
#TRAE TODOS LOS TACTOS
class Tacto_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Tacto.objects.all()
            serializer = Tacto_Serializers(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#TRAE TACTO POR ID
class Tacto_ListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = list(Tacto.objects.filter(id=id).values())
                if len(queryset) > 0: 
                    cows = queryset[0]
                    return Response(cows , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO TACTO
class Tacto_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = Tacto_Serializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ACTUALIZA UN TACTO
class Tacto_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Tacto.objects.get(id = id)
            serializer = Tacto_Serializers(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN GANADO 
class Tacto_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Tacto.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)