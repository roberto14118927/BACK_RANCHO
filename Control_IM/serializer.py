from django.db.models.base import Model
from rest_framework import serializers
from Control_IM.models import Inventario_Insumos


class InventarioInsumos_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario_Insumos
        fields = ('__all__')