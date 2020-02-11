from django.db import models


class Signo(models.Model):
    nombre = models.CharField(max_length=50)
    video = models.URLField()  # Url al Video

    def __str__(self):
        return self.nombre


class VideoEntrenamiento(models.Model):
    signo = models.ForeignKey(Signo, models.CASCADE, 'signo')
    video_entrenamiento = models.URLField(null=False, blank=True)
    fecha_hora_subida = models.DateTimeField(blank=True, auto_now_add=True)


    def __str__(self):
        return 'Video Entrenamiento de:' +self.signo.nombre