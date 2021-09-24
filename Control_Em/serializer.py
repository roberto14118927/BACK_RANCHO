from django.db.models import fields
from rest_framework import routers, serializers, viewsets
from Control_Em.models import Tacto , Control_Empadre


class Empadre_Serializers(serializers.ModelSerializer):
    class Meta: 
        model = Control_Empadre
        fields =  ['id','dia_servicio' ,'mes_servicio' ,
                    'anio_servicio' , 'tipo_servicio' ,'dia_gestacion','mes_gestacion',
                    'anio_gestacion', 'estado_servicio', 'dia_prob_parto' ,'mes_prob_parto',
                    'anio_prob_parto' ,'id_toro' ,'vaca_id' ]
        depth = 1

class Tacto_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Tacto
        fields = ['id', 'detalle' , 'hallazgo' , 'id_empadre']
        depth = 10