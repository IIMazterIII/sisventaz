# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-02 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventaz_app', '0028_auto_20171202_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='producto_str',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
