# Generated by Django 5.1.1 on 2024-11-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAsistencias', '0002_alter_periodoescolar_idperiodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodoescolar',
            name='FechaFin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='periodoescolar',
            name='FechaInicio',
            field=models.DateField(),
        ),
    ]