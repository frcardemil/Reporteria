# Generated by Django 4.1.2 on 2024-06-03 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReporteGeneral',
            fields=[
                ('mes_anno_reporte', models.DateField(primary_key=True, serialize=False, verbose_name='Mes y Año del Reporte')),
                ('entrega_total', models.IntegerField(default=1, verbose_name='Despachos efectuados')),
                ('entrega_a_tiempo', models.IntegerField(default=1, verbose_name='Despachos a tiempo')),
                ('stock_productos', models.IntegerField(default=1, verbose_name='Stock de productos')),
                ('pedido_proveedor', models.IntegerField(default=1, verbose_name='Pedidos a proveedores')),
                ('adquisicion_recibida', models.IntegerField(default=1, verbose_name='Adquisicion a tiempo')),
                ('venta_pedido', models.IntegerField(default=1, verbose_name='Ventas pedidas')),
                ('venta_realizada', models.IntegerField(default=1, verbose_name='Ventas definitivas')),
                ('factura_total', models.IntegerField(default=1, verbose_name='Facturas hechas en total')),
                ('factura_pagada', models.IntegerField(default=1, verbose_name='Facturas pagadas')),
            ],
        ),
    ]
