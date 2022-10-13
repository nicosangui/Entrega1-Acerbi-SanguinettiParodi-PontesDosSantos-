from django.db import models

# Create your models here.

    
class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=20)
    lugar_de_nacimiento = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()
    edad = models.IntegerField()
    equipo_actual = models.CharField(max_length=20)
    posicion = models.CharField(max_length=20)
    altura = models.DecimalField(decimal_places=2, max_digits=3)
    peso = models.DecimalField(decimal_places=2, max_digits=5)