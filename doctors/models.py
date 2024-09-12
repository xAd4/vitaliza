from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
# Method Security 1
def custom_upload_to(instance, filename):
    if instance.pk:  # Verifica si la instancia ya tiene una pk
        old_instance = Doctor.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'doctors/' + filename

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100, verbose_name="Nombre del doctor")
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Imágen del doctor")
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
    
@receiver(post_delete, sender=Doctor)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)