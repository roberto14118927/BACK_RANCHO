from django.db.models import fields, query
from rest_framework import routers, serializers, viewsets

from Control_G.models import Raza , Ganado


class RazaSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Raza
        fields = ['id' , 'raza']
        depth = 10


class GanadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ganado
        fields = ['id', 'nombre', 'sexo','id_raza', 'num_economico','num_registro' ,'num_siniga' ,'comentarios' ,'dia_nacimiento'  
        ,'mes_nacimiento' ,'anio_nacimiento','padre'  ,'madre'  ,'dia_entrada_hato' ,'mes_entrada_hato' ,'anio_entrada_hato' ,
        'estado' ,'condicion_estadia']
        depth = 10

