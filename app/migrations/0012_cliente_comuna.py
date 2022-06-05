# Generated by Django 3.2.11 on 2022-06-04 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_cliente_comuna'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='comuna',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.comuna'),
            preserve_default=False,
        ),
    ]
