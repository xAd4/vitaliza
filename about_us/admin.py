from django.contrib import admin
from .models import AboutInfo

# Register your models here.
class Read_only_fields_admin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

# Registrando módelo
admin.site.register(AboutInfo, Read_only_fields_admin)