from django.db.models import fields
from rest_framework import serializers
from apps.Ganado.Control_Ganado.models import Ganado

class GanadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ganado
        fields = '__all__'


class GanadoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ganado
        fields = '__all__'
        depth = 10


