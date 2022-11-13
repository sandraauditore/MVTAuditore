from django.db import models

# Create your models here.

class familiares(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    Edad = models.IntegerField()
    Fecha_nacimiento = models.DateField()

