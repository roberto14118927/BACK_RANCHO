from django.db.models import fields
from rest_framework import routers, serializers, viewsets
from Control_T.models import Inventario_termo , Empadre_Termo


class Termo_Serializers(serializers.ModelSerializer):
    class Meta: 
        model = Inventario_termo
        fields = ('__all__')


class Empadre_termo_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Empadre_Termo
        fields = ('__all__')