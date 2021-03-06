# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-03 18:01
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20180403_2026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-priority', 'name'), 'verbose_name': 'Questions section', 'verbose_name_plural': 'Questions sections'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-priority', 'text'), 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Category name'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Answer text'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questions.Category', verbose_name='Questions section'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Show on main'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Is published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255, verbose_name='Question text'),
        ),
    ]
