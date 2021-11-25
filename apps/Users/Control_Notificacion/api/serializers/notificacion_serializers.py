from rest_framework import serializers
from apps.Users.Control_Notificacion.models import Control_Notificacion

class NotiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Control_Notificacion
        fields = '__all__'


class NotiListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Control_Notificacion
        fields = ['id' , 'asunto' , 'mensaje' , 'id_usuario_emisor' , 'id_usuario_receptor']
        depth = 50