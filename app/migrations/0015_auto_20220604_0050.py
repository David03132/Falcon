# Generated by Django 3.2.11 on 2022-06-04 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_cliente_comuna'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='abreviatura',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='capital',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
