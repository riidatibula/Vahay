# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vahaysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=1000)),
            ],
        ),
    ]
