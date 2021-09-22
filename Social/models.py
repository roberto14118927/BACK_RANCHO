from django.db import models

class Profile(models.Model):

    nombre = models.CharField(max_length=254, null = False)
    apellido_paterno = models.CharField(max_length=254, null = False)
    apellido_materno = models.CharField(max_length=254, null = False)
    usuario = models.CharField(max_length=254, null = False)
    password = models.CharField(max_length=254, null = False)
    email = models.EmailField(max_length=254 , null= False)
    roll = models.CharField(max_length=254, null = False)

    def __str__(self):
        return self.name

    class Meta: 
        db_table = 'Usuario'