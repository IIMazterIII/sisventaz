# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-02 18:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventaz_app', '0024_remove_ventadetalle_descuento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ventadetalle',
            options={'ordering': ['venta_fk'], 'verbose_name': 'VentaDetalle', 'verbose_name_plural': 'VentaDetalles'},
        ),
    ]
