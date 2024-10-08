# Generated by Django 5.1.1 on 2024-09-09 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100, verbose_name='Nombre del doctor')),
                ('facebook', models.URLField(max_length=100, verbose_name='Facebook del doctor')),
                ('twitter', models.URLField(max_length=100, verbose_name='Twitter del doctor')),
                ('instagram', models.URLField(max_length=100, verbose_name='Instagram del doctor')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctores',
            },
        ),
    ]
