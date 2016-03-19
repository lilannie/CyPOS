# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCourses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.TextField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('numCredits', models.IntegerField()),
                ('prereqs', models.ManyToManyField(related_name='_testcourses_prereqs_+', to='base.TestCourses')),
            ],
        ),
        migrations.CreateModel(
            name='TestDepartments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('acronym', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
            ],
        ),
    ]
