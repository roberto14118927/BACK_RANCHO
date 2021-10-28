from rest_framework import serializers

from apps.Ganado.Control_Peso.models import Peso_Ganando

class PesoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Peso_Ganando
        fields = '__all__'


class PesoListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Peso_Ganando
        fields = ['id' , 'id_ganado', 'fecha_peso' , 'ganancia_peso_mensual_kilo' ,
                 'ganancia_peso_mensual_porcentaje' , 'estado_vaca',
                 'peso']
        depth = 10