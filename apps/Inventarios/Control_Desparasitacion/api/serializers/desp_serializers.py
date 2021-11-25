from rest_framework import serializers
from apps.Inventarios.Control_Desparasitacion.models import Control_Desparasitacion


class DespSerializers(serializers.ModelSerializer):
    class Meta:
        model = Control_Desparasitacion
        fields = '__all__'


class DespListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Control_Desparasitacion
        fields = ['id' , 'id_medicamento' , 'id_ganado' , 'fecha_desparacitacion']
        depth = 10