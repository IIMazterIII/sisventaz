# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-02 00:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventaz_app', '0010_auto_20171201_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cajero',
            name='numero_piso',
        ),
    ]
