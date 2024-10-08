# Generated by Django 5.1.1 on 2024-09-12 15:01

import treatment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=treatment.models.custom_upload_to, verbose_name='Imagen de prueba')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Tratamiento',
                'verbose_name_plural': 'Tratamientos',
            },
        ),
    ]
