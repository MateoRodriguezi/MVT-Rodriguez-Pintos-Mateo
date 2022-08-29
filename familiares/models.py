from django.db import models

class datos_familia(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128) 
    fecha_nacimiento = models.DateField()
    altura = models.IntegerField()