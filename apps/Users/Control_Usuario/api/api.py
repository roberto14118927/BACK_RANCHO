from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.Users.Control_Usuario.models import User
from apps.Users.Control_Usuario.api.serializer import  UserSerializer , UserListSerializer


@api_view(['GET' , 'POST'])
def user_api_view(request):

    if request.method == 'GET':
        queryset = User.objects.all().order_by('id')
        serializer = UserListSerializer(queryset, many= True)
        return Response(data = serializer.data , status= status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        return Response(serializer.errors ,status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET' , 'PUT' , 'DELETE'])
def user_detail_view(request , pk=None):

    #Get by id
    if request.method == 'GET':
        user = User.objects.filter(id = pk).first()
        serializer = UserSerializer(user)
        return Response(data = serializer.data , status= status.HTTP_200_OK)


    #Update
    elif request.method == 'PUT':
        user = User.objects.filter(id = pk).first()
        serializer = UserSerializer(user , data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        
        return Response(serializer.errors ,status = status.HTTP_400_BAD_REQUEST)


    #Delete
    elif request.method == 'DELETE':
        user = User.objects.filter(id = pk).first()
        user.delete()
        return Response(status= status.HTTP_200_OK)