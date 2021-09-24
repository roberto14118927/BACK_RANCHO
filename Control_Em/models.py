from django.db import models
from django.db import models
from django.db.models.fields import CharField
from Control_G.models import Ganado


# Create your models here.

class Control_Empadre(models.Model):
    
    dia_servicio = models.IntegerField()
    mes_servicio = models.IntegerField()
    anio_servicio = models.IntegerField()

    tipo_servicio = models.CharField(max_length=254)
    dia_gestacion = models.IntegerField()
    mes_gestacion = models.IntegerField()
    anio_gestacion = models.IntegerField()

    estado_servicio = models.CharField(max_length=254)
    dia_prob_parto = models.IntegerField()
    mes_prob_parto= models.IntegerField()
    anio_prob_parto = models.IntegerField()

    id_toro = models.ForeignKey(Ganado , on_delete=models.CASCADE , related_name='id_vaca')
    vaca_id = models.ForeignKey(Ganado , on_delete=models.CASCADE , related_name='id_toro')


    def __str__(self):
        return self.tipo_servicio

    class Meta: 
        db_table = 'Control_empadre'


class Tacto (models.Model):
    detalle = models.CharField(max_length=254)
    hallazgo = models.CharField(max_length=254)
    id_empadre = models.ForeignKey(Control_Empadre, on_delete= models.CASCADE)

    def __str__(self):
        return self.datalle

    class Meta: 
        db_table = 'Tacto'
