# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-02 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventaz_app', '0025_auto_20171202_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventadetalle',
            name='ingresodetalles_fk',
        ),
        migrations.RemoveField(
            model_name='ventadetalle',
            name='venta_fk',
        ),
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='venta',
            name='ingresos_fk',
            field=models.ManyToManyField(blank=True, null=True, related_name='ingreso_related', to='ventaz_app.Ingreso'),
        ),
        migrations.AddField(
            model_name='venta',
            name='precio_venta',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='VentaDetalle',
        ),
    ]
