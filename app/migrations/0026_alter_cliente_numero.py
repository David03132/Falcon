# Generated by Django 3.2.11 on 2022-06-05 00:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_cliente_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Número'),
        ),
    ]
