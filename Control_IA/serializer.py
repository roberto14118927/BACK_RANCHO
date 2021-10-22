from django.db.models.base import Model
from rest_framework import serializers
from Control_IA.models import Inventario_Alimentos


class InventarioAlimentos_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario_Alimentos
        fields = ('__all__')