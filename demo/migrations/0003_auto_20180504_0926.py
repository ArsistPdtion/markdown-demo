# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-04 01:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_examplemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplemodel',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examplemodel',
            name='modify_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]