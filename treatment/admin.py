from django.contrib import admin
from .models import Treatment

# Register your models here.
class Read_only_fields_admin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

# Registrando modelo
admin.site.register(Treatment, Read_only_fields_admin)
