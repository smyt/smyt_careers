# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 05:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_vacancy_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='is_hot',
            new_name='is_main',
        ),
    ]
