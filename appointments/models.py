from django.db import models
from doctors.models import Doctor
from departments.models import Deparment

# Create your models here.

class Appointment(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Nombre del paciente")
    department = models.ForeignKey(Deparment, on_delete=models.CASCADE, verbose_name="Nombre del departamento deseado")
    phone_number = models.CharField(max_length=100, verbose_name="Número de teléfono")
    symptoms = models.CharField(max_length=600, verbose_name="Síntomas")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")


    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"

    def __str__(self):
        return f"{self.full_name} - {self.doctor} - {self.department}"
    