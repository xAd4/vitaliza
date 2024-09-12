from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Method Security 1
def custom_upload_to(instance, filename):
    if instance.pk:  # Verifica si la instancia ya tiene una pk
        old_instance = Treatment.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'treatment/' + filename

# Create your models here.
class Treatment(models.Model):
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Imagen de prueba")
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Tratamiento"
        verbose_name_plural = "Tratamientos"

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Treatment)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)