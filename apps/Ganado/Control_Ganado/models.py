from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


class Raza(models.Model):
    raza = models.CharField(max_length=254 , unique=True)

    def __str__(self):
        return self.raza 

    class Meta: 
        db_table = 'Raza'


class Ganado(models.Model):

    nombre = models.CharField(max_length=254 , unique=True)
    sexo = models.CharField(max_length=254)
    #foreing Key 
    id_raza = models.ForeignKey(Raza, on_delete= SET_NULL, related_name="id_raza", null=True)  
   
    num_economico = models.CharField(max_length=254 , null=True , blank=True , unique=True)
    num_registro = models.CharField(max_length=254 , null=True , blank=True , unique=True)
    num_siniga = models.CharField(max_length=254 , null=True , blank=True, unique=True)
    comentarios = models.CharField(max_length=254, null=True , blank=True)
    fecha_nacimiento =  models.CharField(max_length=10 , null=True)
    
    padre = models.CharField(max_length=254 , blank=True)
    madre = models.CharField(max_length=254 , blank=True)
    
    fecha_entrada_hato = models.CharField(max_length=10, null=True)
    estado = models.CharField(max_length=254)
    condicion_estadia = models.CharField(max_length=254)
  

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'Ganado'
