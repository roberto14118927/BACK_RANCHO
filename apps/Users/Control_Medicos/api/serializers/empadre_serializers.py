from rest_framework import serializers
from apps.Users.Control_Medicos.models import Empadre_medico 


class EmpadreListSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Empadre_medico
        fields = '__all__'
        depth = 10

class EmpadreMedicoSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Empadre_medico
        fields = '__all__'

