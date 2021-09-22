from django.db.models import fields
from rest_framework import routers, serializers, viewsets

from Control_G.models import Raza , Ganado


class RazaSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Raza
        fields = ('__all__')


class GanadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ganado
        fields = ('__all__')