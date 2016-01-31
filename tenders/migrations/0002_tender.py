# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date published')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenders.Contractor')),
                ('procurer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenders.Procurer')),
            ],
        ),
    ]
