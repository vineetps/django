# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-24 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20200524_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedetails',
            name='share_price',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]
