# Generated by Django 5.1.1 on 2024-09-09 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='choose_date',
        ),
    ]
