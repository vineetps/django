# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-24 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_sharedetails_share_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedetails',
            name='short_name',
            field=models.CharField(default=123, max_length=8),
            preserve_default=False,
        ),
    ]
