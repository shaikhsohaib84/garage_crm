# Generated by Django 3.2.5 on 2022-01-23 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garageApp', '0002_alter_vehicle_number_plate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='billing',
            new_name='bill',
        ),
        migrations.AlterModelTable(
            name='bill',
            table='bill',
        ),
    ]