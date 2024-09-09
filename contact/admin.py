from django.contrib import admin
from .models import Contact

# Register your models here.

# Configuración sólo lectura
class Read_only_fields_admin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

# Registrando módelo
admin.site.register(Contact, Read_only_fields_admin)
