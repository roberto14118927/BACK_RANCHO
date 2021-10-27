from django.db.models.base import Model
from rest_framework import serializers
from apps.Inventarios.Control_IMateriales.models import Inventario_Materiales


class InventarioMateriales_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario_Materiales
        fields = ('__all__')