# Generated by Django 5.1.1 on 2024-09-09 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nombre del paciente')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Número de teléfono')),
                ('symptoms', models.CharField(max_length=600, verbose_name='Síntomas')),
                ('choose_date', models.DateField(verbose_name='Fecha de cita')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.deparment', verbose_name='Nombre del departamento deseado')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor', verbose_name='Nombre del doctor deseado')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
            },
        ),
    ]
