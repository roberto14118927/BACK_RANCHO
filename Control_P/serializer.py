from django.db.models import fields
from rest_framework import serializers
from Control_P.models import Peso_Ganando , Vacas_asociadas , Enfermedades_Ganado


class Peso_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Peso_Ganando
        fields = ('__all__')

class Enfermedades_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedades_Ganado
        fields = ('__all__')
    
class Vacas_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Vacas_asociadas
        fields = ('__all__')