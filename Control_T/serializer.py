from rest_framework import serializers
from Control_T.models import Inventario_termo , Empadre_Termo


class Termo_Serializers(serializers.ModelSerializer):
    class Meta: 
        model = Inventario_termo
        fields = ['id' , 'num_canastilla' , 'nombre_toro' , 'raza' , 'descripcion', 
                'cantidad' , 'comentario' , 'num_termo']
        depth=10

class Termo_Create_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Inventario_termo
        fields = ('__all__')


class Empadre_termo_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Empadre_Termo
        fields = ['id' , 'id_empadre' , 'id_inv_termo']
        depth = 10