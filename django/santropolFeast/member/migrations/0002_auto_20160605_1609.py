# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_fix161f'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Address', verbose_name='address'),
        ),
    ]
