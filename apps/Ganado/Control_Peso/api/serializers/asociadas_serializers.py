from rest_framework import serializers
from apps.Ganado.Control_Peso.models import Vacas_asociadas


class AsociadasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vacas_asociadas
        fields = '__all__'

    
class AsociadasListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vacas_asociadas
        fields = ['id' , 'id_enfermedad' , 'id_ganado' ]
        depth = 10