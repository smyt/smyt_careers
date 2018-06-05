# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-03 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo_pages', '0002_auto_20180205_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seopage',
            options={'verbose_name': 'Site page', 'verbose_name_plural': 'Site pages'},
        ),
        migrations.AlterField(
            model_name='seopage',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title page'),
        ),
        migrations.AlterField(
            model_name='seopage',
            name='type_page',
            field=models.CharField(choices=[('main_page', 'Site main page'), ('vacancy_list', 'Site page with vacancy list'), ('vacancy_page', 'Site page with vacancy page'), ('question_list', 'Site page with question list')], max_length=255, unique=True, verbose_name='Type page'),
        ),
    ]