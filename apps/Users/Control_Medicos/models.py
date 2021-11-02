from django.db import models
from django.db.models.deletion import SET_NULL
from apps.Ganado.Control_Empadre.models import Control_Empadre

class Medico_Especialista (models.Model):

    nombre = models.CharField(max_length=254)

    def __str__(self):
        return str(self.id)

    class Meta: 
        db_table = 'Medico_Especialista'


class Empadre_medico(models.Model):

    id_empadre = models.ForeignKey(Control_Empadre , on_delete= SET_NULL , null=True)
    id_medico = models.ForeignKey(Medico_Especialista , on_delete= SET_NULL , null=True)

    def __str__(self):
        return str(self.id_empadre)

    class Meta: 
        db_table = 'Empadre_Medico'