# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0006_secretary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateTimeField()),
                ('patient_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
                ('secretary_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Secretary')),
                ('specialist_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Specialist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]