from rest_framework import serializers
from apps.Inventarios.Control_Vacunacion.models  import Control_Vacunas


class VacunaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Control_Vacunas
        fields = '__all__'


class VacunaListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Control_Vacunas
        fields = ['id' , 'id_medicamento' , 'id_ganado' , 'fecha_vacunacion']
        depth = 10