from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.utils.decorators import method_decorator


from Control_M.serializer import Empadre_Serializers , Medico_Serializers
from Control_M.models import Empadre_medico , Medico_Especialista


#------------ VIEWS PARA EMPADRE ------------------
#TRAE TODOS LOS EMPADRES
class Empadre_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Empadre_medico.objects.all()
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
                queryset = list(Empadre_medico.objects.filter(id=id).values())
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
            cows = Empadre_medico.objects.get(id = id)
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
            user = Empadre_medico.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)



#----------------VIEWS PARA MEDICOS ------------------------------------------

#TRAE TODOS LOS MEDICOS
class Medico_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Medico_Especialista.objects.all()
            serializer = Medico_Serializers(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#TRAE TACTO POR ID
class Medico_ListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = list(Medico_Especialista.objects.filter(id=id).values())
                if len(queryset) > 0: 
                    cows = queryset[0]
                    return Response(cows , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO MEDICO
class Medico_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = Medico_Serializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ACTUALIZA UN MEDICO
class Medico_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Medico_Especialista.objects.get(id = id)
            serializer = Medico_Serializers(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN MEDICO 
class Medico_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Medico_Especialista.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)