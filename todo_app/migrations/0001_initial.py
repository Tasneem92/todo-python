# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-15 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=256)),
                ('description', models.TextField(db_column='Description')),
            ],
            options={
                'db_table': 'Todo',
                'managed': True,
            },
        ),
    ]
