from django.db import models

# Create your models here.
class Viaje(models.Model):
               nombre=models.CharField
               categoria=models.IntegerField()

class Pasajero(models.Model):
        nombre=models.CharField (max_length=20)
        apellido=models.CharField(max_length=20)
        email=models.EmailField

class Chofer(models.Model):
        nombre=models.CharField (max_length=20)
        apellido=models.CharField(max_length=20)
        unidadl=models.CharField

class Viaje(models.Model):
        Destino=models.CharField (max_length=40)
        Costo=models.CharField(max_length=20)
        Encuesta=models.CharField
        