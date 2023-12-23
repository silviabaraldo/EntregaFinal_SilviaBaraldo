from django.db import models

# Create your models here.

class Pasajero(models.Model):
        nombre=models.CharField (max_length=20)
        apellido=models.CharField(max_length=20)
        email=models.EmailField

class Chofer(models.Model):
        nombre=models.CharField (max_length=20)
        apellido=models.CharField(max_length=20)
        unidad=models.CharField
        