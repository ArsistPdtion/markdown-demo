# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-04 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', mdeditor.fields.MDTextField()),
            ],
        ),
    ]
