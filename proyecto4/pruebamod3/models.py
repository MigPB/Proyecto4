from django.db import models

# Create your models here.
from django.db import models

class Lugar(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre

class Restaurante(models.Model):
    lugar = models.OneToOneField(Lugar, on_delete=models.CASCADE, related_name='restaurante')
    especialidad = models.CharField(max_length=100)
    horario_apertura = models.TimeField()

    def __str__(self):
        return f"Restaurante en {self.lugar.nombre}"

class Camarero(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='camareros')
    nombre = models.CharField(max_length=100)
    experiencia = models.IntegerField(help_text="Años de experiencia")

    def __str__(self):
        return f"{self.nombre} - {self.restaurante.lugar.nombre}"
