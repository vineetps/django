# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-24 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=8, unique=True)),
                ('category', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShareDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shares_bought', models.IntegerField()),
                ('short_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.CompanyDetails')),
            ],
        ),
        migrations.RemoveField(
            model_name='accessrecord',
            name='name',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='WebPage',
        ),
        migrations.AddField(
            model_name='companydetails',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.CompanyName'),
        ),
    ]
