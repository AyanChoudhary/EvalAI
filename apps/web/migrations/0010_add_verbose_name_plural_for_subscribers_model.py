# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-05 07:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_added_subscribers_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribers',
            options={'verbose_name_plural': 'Subscribers'},
        ),
    ]