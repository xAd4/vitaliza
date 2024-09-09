from django.contrib import admin
from .models import Appointment

# Register your models here.

# Configuración sólo lectura
class Read_only_fields_admin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

# Registrando modelo
admin.site.register(Appointment, Read_only_fields_admin)
