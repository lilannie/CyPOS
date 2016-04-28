# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_semesters_electives'),
    ]

    operations = [
        migrations.AddField(
            model_name='substitutes',
            name='courseSubOf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='substitude_courseSubOf', to='base.Courses'),
        ),
    ]
