# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-02 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympians', '0002_auto_20191102_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='olympian',
            name='medal',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
    ]
