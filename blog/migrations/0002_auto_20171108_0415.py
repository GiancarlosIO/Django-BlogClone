# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
