# Generated by Django 3.2.11 on 2022-06-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_cliente_depto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['id'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'CLIENTES'},
        ),
        migrations.AlterModelOptions(
            name='comuna',
            options={'ordering': ['id'], 'verbose_name': 'Comuna', 'verbose_name_plural': 'COMUNAS'},
        ),
        migrations.AlterModelOptions(
            name='envio',
            options={'ordering': ['id'], 'verbose_name': 'Envio', 'verbose_name_plural': 'ENVIOS'},
        ),
        migrations.AlterModelOptions(
            name='metodo_pago',
            options={'ordering': ['id'], 'verbose_name': 'Metodo pago', 'verbose_name_plural': 'METODO_PAGOS'},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'ordering': ['id'], 'verbose_name': 'Provincia', 'verbose_name_plural': 'PROVINCIA'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['id'], 'verbose_name': 'Region', 'verbose_name_plural': 'REGIONES'},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={'ordering': ['id'], 'verbose_name': 'Venta', 'verbose_name_plural': 'VENTAS'},
        ),
        migrations.RemoveField(
            model_name='venta',
            name='email_venta',
        ),
        migrations.AlterField(
            model_name='detalle_ingreso',
            name='precio_compra',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='detalle_ingreso',
            name='precio_venta',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='detalle_ingreso',
            name='stock_actual',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='detalle_ingreso',
            name='stock_inicial',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterModelTable(
            name='carrito_compras',
            table='CARRITO_COMPRAS',
        ),
        migrations.AlterModelTable(
            name='categorias',
            table='CATEGORIA',
        ),
        migrations.AlterModelTable(
            name='detalle_ingreso',
            table='DETALLE_INGRESO',
        ),
        migrations.AlterModelTable(
            name='ingreso',
            table='INGRESO',
        ),
        migrations.AlterModelTable(
            name='marcas',
            table='MARCA',
        ),
        migrations.AlterModelTable(
            name='productos',
            table='PRODUCTOS',
        ),
        migrations.AlterModelTable(
            name='proveedor',
            table='PROVEEDOR',
        ),
        migrations.AlterModelTable(
            name='trabajador',
            table='TRABAJADOR',
        ),
        migrations.AlterModelTable(
            name='venta',
            table='VENTA',
        ),
    ]
