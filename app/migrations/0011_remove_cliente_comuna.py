# Generated by Django 3.2.11 on 2022-06-04 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_cliente_comuna'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='comuna',
        ),
    ]
