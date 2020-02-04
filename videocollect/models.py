from django.db import models


class Signo(models.Model):
    nombre = models.CharField(max_length=50)
    video = models.URLField()  # Url al Video


class VideoEntrenamiento(models.Model):
    signo = models.ForeignKey(Signo, models.CASCADE, 'signo')
    video_entrenamiento = models.FileField()
    fecha_hora_subida = models.DateTimeField(blank=True, auto_now_add=True)
