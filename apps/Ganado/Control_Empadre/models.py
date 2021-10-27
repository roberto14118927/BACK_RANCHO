from django.db import models
from django.db import models
from django.db.models.deletion import SET, SET_NULL
from apps.Ganado.Control_Ganado.models import Ganado


# Create your models here.

class Control_Empadre(models.Model):
    
    fecha_servicio = models.CharField(max_length=10 , null=True)
    tipo_servicio = models.CharField(max_length=254)
    
    fecha_gestacion =  models.CharField(max_length=10, null=True)
    estado_servicio = models.CharField(max_length=254)
    
    fecha_parto = models.CharField(max_length=10 , null=True)

    #id_toro = models.ForeignKey(Ganado , on_delete=models.CASCADE , related_name='id_vaca')
    #vaca_id = models.ForeignKey(Ganado , on_delete=models.CASCADE , related_name='id_toro')

    id_toro = models.ForeignKey(Ganado ,on_delete= SET_NULL, related_name='id_vaca' , null=True)
    vaca_id = models.ForeignKey(Ganado , on_delete= SET_NULL , related_name='id_toro', null=True)


    def __str__(self):
        return self.tipo_servicio

    class Meta: 
        db_table = 'Control_empadre'


class Tacto (models.Model):
    detalle = models.CharField(max_length=254)
    hallazgo = models.CharField(max_length=254)
    id_empadre = models.ForeignKey(Control_Empadre, on_delete= SET_NULL , null=True)
    fecha = models.CharField(max_length=10 , null=True)

    def __str__(self):
        return self.datalle

    class Meta: 
        db_table = 'Tacto'
