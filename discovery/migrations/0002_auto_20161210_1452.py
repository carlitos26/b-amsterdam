# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discovery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='opening_hours',
            field=models.CharField(max_length=450, null=True),
        ),
    ]
