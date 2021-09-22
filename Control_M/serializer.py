from django.db.models import fields
from rest_framework import routers, serializers, viewsets
from Control_M.models import Medico_Especialista , Empadre_medico


class Empadre_Serializers(serializers.ModelSerializer):
    class Meta: 
        model = Empadre_medico
        fields = ('__all__')


class Medico_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Medico_Especialista
        fields = ('__all__')