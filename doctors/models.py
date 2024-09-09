from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100, verbose_name="Nombre del doctor")
    facebook = models.URLField(max_length=100, verbose_name="Facebook del doctor")
    twitter = models.URLField(max_length=100, verbose_name="Twitter del doctor")
    instagram = models.URLField(max_length=100, verbose_name="Instagram del doctor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"

    def __str__(self):
        return self.doctor_name