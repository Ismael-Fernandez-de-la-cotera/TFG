from django.db import models

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    respuesta1 = models.CharField(max_length=100)
    respuesta2 = models.CharField(max_length=100)
    respuesta3 = models.CharField(max_length=100)
    respuesta4 = models.CharField(max_length=100)

    def __str__(self):
        return self.pregunta


class Respuesta(models.Model):
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE, null=True, blank=True)
    respuesta = models.TextField()
    nombre_usuario = models.CharField(max_length=255, null=True, blank=True)
    puntuacion = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    Esta_de_examenes = models.BooleanField(null=True)
    edad = models.IntegerField(null=True, blank=True)
    sexo = models.CharField(
        max_length=25,
        choices=[
            ('Hombre', 'Hombre'),
            ('Mujer', 'Mujer'),
            ('Prefiero no decirlo', 'Prefiero no decirlo')
        ],
        null=True, blank=True
    )

    class Meta:
        unique_together = ('nombre_usuario', 'pregunta')

    def __str__(self):
        return f"{self.nombre_usuario} - {self.pregunta}: {'Sí' if self.Esta_de_examenes else 'No'}"

class FeedbackFinal(models.Model):
    nombre_usuario = models.CharField(max_length=255, unique=True)
    Ha_resultado_util = models.BooleanField(null=True)
    Se_ha_entendido = models.BooleanField(null=True)
    De_acuerdo_puntuaciones = models.BooleanField(null=True)
    De_acuerdo_final = models.BooleanField(null=True)
    Lo_recomienda = models.BooleanField(null=True)

    def __str__(self):
        return f"Feedback de {self.nombre_usuario}"
