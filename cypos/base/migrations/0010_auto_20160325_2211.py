# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20160324_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numCredits', models.IntegerField(blank=True, default=b'0', null=True)),
                ('courses', models.ManyToManyField(related_name='courses', to='base.Courses')),
            ],
        ),
        migrations.AddField(
            model_name='pos',
            name='semesters',
            field=models.ManyToManyField(related_name='semesters', to='base.Semesters'),
        ),
    ]
