# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createnetwork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkanalysis',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='AnalysisName',
        ),
    ]
