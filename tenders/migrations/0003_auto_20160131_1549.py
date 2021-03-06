# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0002_tender'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='contractor',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='procurer',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='procurer',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
