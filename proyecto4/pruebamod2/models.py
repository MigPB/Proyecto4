from django.db import models

# Create your models here.
from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    publicacion = models.OneToOneField(Publicacion, on_delete=models.CASCADE, related_name='noticia')
    autor = models.CharField(max_length=100)
    fuente = models.CharField(max_length=200)

    def __str__(self):
        return f"Noticia de {self.publicacion.titulo}"
