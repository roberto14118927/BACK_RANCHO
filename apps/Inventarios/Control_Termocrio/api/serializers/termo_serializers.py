from rest_framework import serializers
from apps.Inventarios.Control_Termocrio.models import Inventario_termo


class InventarioTermoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario_termo
        fields = ('__all__')
        depth = 10


class InventarioTermoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario_termo
        fields = ('__all__')