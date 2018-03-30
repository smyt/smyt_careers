# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seopage',
            name='type_page',
            field=models.CharField(choices=[('main_page', 'Главная страница сайта'), ('vacancy_list', 'Страница со списком вакансий'), ('vacancy_page', 'Cтраница с вакансией сайта'), ('question_list', 'Страница со списком вопросов')], max_length=255, unique=True, verbose_name='Тип страницы'),
        ),
    ]
