# Generated by Django 4.1.3 on 2023-01-08 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0002_mascota_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='antiguedad',
            field=models.IntegerField(),
        ),
    ]