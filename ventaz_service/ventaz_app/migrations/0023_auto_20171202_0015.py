# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-02 05:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventaz_app', '0022_auto_20171201_2348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingreso',
            options={'ordering': ['fecha_ingreso'], 'verbose_name': 'Ingreso', 'verbose_name_plural': 'Ingresos'},
        ),
    ]
