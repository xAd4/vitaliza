from django.db import models

# Create your models here.

class Deparment(models.Model):
    department_name = models.CharField(max_length=100, verbose_name="Nombre del departamento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.department_name