# Generated by Django 4.2.6 on 2023-11-27 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas_app', '0003_alter_reserva_cantidad_personas_alter_reserva_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='hora',
            field=models.CharField(max_length=15),
        ),
    ]
