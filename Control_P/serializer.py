from django.db.models import fields
from rest_framework import serializers
from Control_P.models import Peso_Ganando , Vacas_asociadas , Enfermedades_Ganado


class Peso_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Peso_Ganando
        fields = ['id' , 'id_ganado', 'fecha_peso' , 'ganancia_peso_mensual_kilo' ,
                 'ganancia_peso_mensual_porcentaje' , 'estado_vaca',
                 'peso']
        depth = 10

class Enfermedades_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedades_Ganado
        fields = ['id' , 'nombre' , 'numero_casos',
        'numero_animales' , 'porcentaje_infectado',
        'fecha_detectado','vacas' , 'toros']
        depth = 10

class Create_enfermedad(serializers.ModelSerializer):
    class Meta:
        model = Enfermedades_Ganado
        fields = ('__all__')
    
class Vacas_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Vacas_asociadas
        fields = ['id' , 'id_enfermedad' , 'id_ganado' ]
        depth = 10