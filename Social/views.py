from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator

from Social.serializer import ProfileSerializers
from Social.models import Profile


#TRAE TODOS LOS USUARIOS
class ProfileList(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request , id=0):
        try:
            queryset = Profile.objects.all()
            serializer = ProfileSerializers(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#TRAE USUARIOS POR IDs
class ProfileListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = list(Profile.objects.filter(id=id).values())
                if len(queryset) > 0: 
                    user = queryset[0]
                    return Response(user , status= status.HTTP_200_OK)
                else:
                    message = {"User not found or not exist"}
                    return Response(message)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                


#CREA UN NUEVO USUARIO
class ProfileCreate(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = ProfileSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                message = {'User created!'}
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ACTUALIZA UN USUARIO
class ProfileUpdate(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            user = Profile.objects.get(id = id)
            serializer = ProfileSerializers(user , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN USUARIO 
class ProfileDelete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Profile.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)