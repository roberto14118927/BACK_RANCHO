from rest_framework import serializers
from apps.Ganado.Control_Ganado.models import Raza , Ganado


class RazaSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Raza
        fields = ['id' , 'raza']
        depth = 10


class GanadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ganado
        fields = ['id', 'nombre', 'sexo','id_raza', 'num_economico','num_registro' ,'num_siniga' ,'comentarios' ,
        'fecha_nacimiento','padre'  ,'madre'  ,'fecha_entrada_hato' ,
        'estado' ,'condicion_estadia']
        depth = 10

