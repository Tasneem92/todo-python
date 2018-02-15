# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-15 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_auto_20180215_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomirror',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='todo_app.Todo'),
        ),
        migrations.AlterField(
            model_name='todomirror',
            name='mdescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='todo_app.Todo', to_field='description'),
        ),
        migrations.AlterField(
            model_name='todomirror',
            name='mname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='todo_app.Todo', to_field='name'),
        ),
    ]
