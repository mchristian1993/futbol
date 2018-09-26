from django.db import models
class Equipos(models.Model):
    nombre_equipo = models.CharField(max_length=255, null=False)
    liga = models.CharField(max_length=255, null=False)
    tecnico = models.CharField(max_length=255, null=False)

# Create your models here.
