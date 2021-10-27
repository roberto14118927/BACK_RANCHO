from rest_framework import serializers
from apps.Ganado.Control_Ganado.models import Ganado

class GanadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ganado
        exclude = ['state']


class GanadoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ganado
        exclude = ['state']
        depth = 10


