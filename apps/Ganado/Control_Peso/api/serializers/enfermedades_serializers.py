from rest_framework import serializers
from apps.Ganado.Control_Peso.models import Enfermedades_Ganado

class EnfermedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedades_Ganado
        fields = '__all__'
        

class EnfermedadesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedades_Ganado
        fields = ['id' , 'nombre' , 'numero_casos',
        'numero_animales' , 'porcentaje_infectado',
        'fecha_detectado','vacas' , 'toros']
        depth = 10