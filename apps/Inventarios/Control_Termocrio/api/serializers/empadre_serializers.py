from rest_framework import serializers
from apps.Inventarios.Control_Termocrio.models import Empadre_Termo


class EmpadreTermoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empadre_Termo
        fields = '__all__'


class EmpadreTermoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empadre_Termo
        fields = ['id' , 'id_empadre' , 'id_inv_termo']
        depth = 10