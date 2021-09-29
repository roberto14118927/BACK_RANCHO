from django.db import models
from Control_G.models import Ganado

# Create your models here.

#Modelo para el peso del ganado.
class Peso_Ganando(models.Model):

    id_ganado = models.ForeignKey(Ganado , on_delete= models.CASCADE)  #foreing Key
    fecha_peso = models.DateField()

    ganancia_peso_mensual_kilo = models.FloatField()
    ganancia_peso_mensual_porcentaje = models.FloatField()
    estado_vaca = models.CharField(max_length=254)
    peso = models.FloatField()

    def __str__(self):
        return self.peso

    class Meta: 
        db_table = 'Peso'


#Modelo para las enfermedades registradas.
class Enfermedades_Ganado(models.Model):

    nombre = models.CharField(max_length=254)
    numero_casos = models.IntegerField()
    numero_animales = models.IntegerField()
    porcentaje_infectado = models.FloatField()

    fecha_detectado = models.DateField()

    vacas = models.IntegerField()
    toros = models.IntegerField()
    

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'Enfermedades'

#Modelo para las vacas asociadas a las enfermedades.
class Vacas_asociadas(models.Model):

    id_enfermedad = models.ForeignKey(Enfermedades_Ganado , on_delete= models.CASCADE)
    id_ganado = models.ForeignKey(Ganado , on_delete= models.CASCADE)
    
    class Meta: 
        db_table = 'Vacas_asociadas'