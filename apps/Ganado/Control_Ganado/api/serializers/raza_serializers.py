from apps.Ganado.Control_Ganado.models import Raza
from rest_framework import serializers


class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'


