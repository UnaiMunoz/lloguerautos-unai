from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.marca} {self.model} ({self.matricula})"

class Reserva(models.Model):
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inici = models.DateField()
    data_fi = models.DateField()

    class Meta:
        # Restricción única para combinación de automóvil y fecha de inicio
        unique_together = ('automobil', 'data_inici')

    def clean(self):
        # Validación adicional si es necesario
        if self.data_fi < self.data_inici:
            raise ValidationError("La data de fi no pot ser anterior a la data d'inici")

    def __str__(self):
        return f"Reserva de {self.automobil} per {self.usuari.username} del {self.data_inici} al {self.data_fi}"