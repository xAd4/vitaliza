from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Nombre completo")
    email = models.EmailField(max_length=200, verbose_name="Email")
    phone_number = models.CharField(max_length=100, verbose_name="Número de teléfono")
    message = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return f"{self.full_name} - {self.email} - {self.phone_number}"
