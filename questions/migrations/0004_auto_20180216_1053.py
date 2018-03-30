# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-16 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='priority',
            field=models.PositiveIntegerField(default=0, help_text='Укажите значения от 1 до 100, где у 100 высший приоритет. Если не указать приоритет, он будет равен 0', verbose_name='Приоритет отображения'),
        ),
        migrations.AlterField(
            model_name='question',
            name='priority',
            field=models.PositiveIntegerField(default=0, help_text='Укажите значения от 1 до 100, где у 100 высший приоритет. Если не указать приоритет, он будет равен 0', verbose_name='Приоритет отображения'),
        ),
    ]
