from rest_framework import serializers
from apps.Inventarios.Control_IMedicos.models import Inventario_Insumos


class InventarioInsumosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario_Insumos
        fields = ('__all__')