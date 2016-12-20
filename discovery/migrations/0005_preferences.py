# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discovery', '0004_auto_20161212_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('italian', models.BooleanField(default=False)),
                ('mexican', models.BooleanField(default=False)),
                ('japanese', models.BooleanField(default=False)),
                ('greek', models.BooleanField(default=False)),
                ('american', models.BooleanField(default=False)),
                ('indian', models.BooleanField(default=False)),
                ('french', models.BooleanField(default=False)),
                ('chinese', models.BooleanField(default=False)),
                ('spanish', models.BooleanField(default=False)),
                ('indonesian', models.BooleanField(default=False)),
                ('dutch', models.BooleanField(default=False)),
                ('argentinian', models.BooleanField(default=False)),
                ('pakistanese', models.BooleanField(default=False)),
                ('african', models.BooleanField(default=False)),
                ('vietnamese', models.BooleanField(default=False)),
                ('pancakes', models.BooleanField(default=False)),
                ('international', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'preferences',
            },
        ),
    ]
