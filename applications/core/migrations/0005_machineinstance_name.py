# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180618_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='machineinstance',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
