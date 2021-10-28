from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from apps.Users.Control_Login.api.serializers import UserTokenSerializer

class UserToken(APIView):
    def get(self, request , *args , **kwargs):
        username = request.GET.get('username')

        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(username = username).first()
            )

            return Response({'token': user_token.key })
        except:
            return Response({'error': 'Credenciales enviadas incorrectas'}, status= status.HTTP_400_BAD_REQUEST)


# Create your views here.
class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        
        login_serializer = self.serializer_class(data = request.data , context = {'request' : request})

        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token , created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created: 
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesión exitoso'
                    } , status= status.HTTP_201_CREATED)
                else:
                    token.delete()
                    return Response({
                        'message': 'Hay una sesión iniciada con este usuario.'
                    } , status= status.HTTP_409_CONFLICT)
            else:
                return Response({'message':'Usuario no permitido.'} , status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message':'Usuario o contraseña incorrectos.'} , status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Login response.'} , status= status.HTTP_200_OK)


class Logout(APIView):
    #El front deberá enviar el token para poder hacer el logout.

    def get(self , request , *args , **kwars):
        try:
            token = request.GET.get('token')
            print(token)
            token = Token.objects.filter(key = token).first()
            if token:
                user = token.user

                token.delete()
                session_message = 'Sesión cerrada'
                token_message = 'Token eliminado'

                return Response({'token_message': token_message , 'session_message' : session_message}
                                ,status= status.HTTP_200_OK)

            return Response({'error': 'No se ha encontrado un usuario con estas credenciales.'} ,
                        status= status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No se ha encontrado token en la petición.'} ,
                        status= status.HTTP_409_CONFLICT)
