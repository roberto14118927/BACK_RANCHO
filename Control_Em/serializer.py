from django.db.models import fields
from rest_framework import routers, serializers, viewsets
from Control_Em.models import Tacto , Control_Empadre


class Empadre_Serializers(serializers.ModelSerializer):
    class Meta: 
        model = Control_Empadre
        fields =  ['id','fecha_servicio' ,'tipo_servicio' ,'fecha_gestacion', 
                    'estado_servicio', 'fecha_parto' ,'id_toro' ,'vaca_id' ]
        depth = 10

class Tacto_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Tacto
        fields = ['id', 'detalle' , 'hallazgo' , 'id_empadre' , 'fecha']
        depth = 10