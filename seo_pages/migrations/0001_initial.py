# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeoPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_page', models.CharField(choices=[('MAIN_PAGE', 'Главная страница сайта'), ('VACANCY_LIST', 'Страница со списокм вакансий'), ('VACANCY_PAGE', 'Cтраница с вакансией сайта'), ('QUESTION_LIST', 'Страница со списком вопросов')], max_length=255, unique=True, verbose_name='Тип страницы')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок страницы')),
                ('keywords', models.TextField(verbose_name='Keywords')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Страница сайта',
                'verbose_name_plural': 'Страницы сайта',
            },
        ),
    ]