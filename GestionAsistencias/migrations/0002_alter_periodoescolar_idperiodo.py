# Generated by Django 5.1.1 on 2024-11-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAsistencias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodoescolar',
            name='idPeriodo',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
