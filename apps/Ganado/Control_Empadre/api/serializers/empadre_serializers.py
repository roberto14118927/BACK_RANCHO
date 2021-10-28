
from rest_framework import serializers
from apps.Ganado.Control_Empadre.models import Control_Empadre


class EmpadreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control_Empadre
        fields = '__all__'
        depth = 10


class EmpadreSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Control_Empadre
        fields =  '__all__'
        