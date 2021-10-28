from apps.Ganado.Control_Ganado.models import Raza
from rest_framework import fields, serializers


class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id ,
            'raza': instance.raza
        }
