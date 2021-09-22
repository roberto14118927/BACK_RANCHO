from django.db.models import fields
from rest_framework import routers, serializers, viewsets
from Control_E.models import Tacto , Control_Empadre


class Empadre_Serializers(serializers.ModelSerializer):
    class Meta: 
        model = Control_Empadre
        fields = ('__all__')


class Tacto_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Tacto
        fields = ('__all__')