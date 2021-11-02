from rest_framework import serializers
from apps.Users.Control_Medicos.models import  Medico_Especialista


class MedicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medico_Especialista
        fields = '__all__'
