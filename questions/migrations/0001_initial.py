# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveIntegerField(default=0, verbose_name='Приоритет отображения')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Раздел вопросов',
                'verbose_name_plural': 'Разделы вопросов',
                'ordering': ('-priority', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveIntegerField(default=0, verbose_name='Приоритет отображения')),
                ('text', models.CharField(max_length=255, verbose_name='Текст вопроса')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликован')),
                ('is_main', models.BooleanField(default=False, verbose_name='На главной')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Category', verbose_name='Раздел вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ('-priority', 'text'),
            },
        ),
    ]
