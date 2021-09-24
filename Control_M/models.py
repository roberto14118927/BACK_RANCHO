from django.db import models
from Control_Em.models import Control_Empadre

class Medico_Especialista (models.Model):

    nombre = models.CharField(max_length=254)

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'Medico_Especialista'

class Empadre_medico(models.Model):

    id_empadre = models.ForeignKey(Control_Empadre , on_delete= models.CASCADE)
    id_medico = models.ForeignKey(Medico_Especialista , on_delete= models.CASCADE)

    def __str__(self):
        return self.id_empadre

    class Meta: 
        db_table = 'Empadre_Medico'