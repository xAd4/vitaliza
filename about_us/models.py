from django.db import models

# Create your models here.

class AboutInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Información"
        verbose_name_plural = "Más información"

    def __str__(self):
        return self.title