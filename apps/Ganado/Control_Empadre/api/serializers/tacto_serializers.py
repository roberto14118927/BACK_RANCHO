from rest_framework import serializers
from apps.Ganado.Control_Empadre.models import Tacto


class TactoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tacto
        fields = '__all__'
        depth = 10

class TactoSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Tacto
        fields =  '__all__'
        