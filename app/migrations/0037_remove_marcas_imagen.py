# Generated by Django 4.0.3 on 2022-06-10 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20220605_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marcas',
            name='imagen',
        ),
    ]