# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0015_auto_20151020_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='code_design_rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], help_text='Оценка върху уменията на кандидата да "съставя програми" и да разбива нещата по парчета + базово OOP', default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='code_skills_rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], help_text='Оценка върху уменията на кандидата да пише код и знанията му върху базови алгоритми', default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='fit_attitude_rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], help_text='Оценка на интервюиращия в зависимост от усета му за човека (става ли за курса)', default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher_comment',
            field=models.TextField(blank=True, null=True, help_text='Коментар на интервюиращия за цялостното представяне на кандидата'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='skype',
            field=models.CharField(max_length=50, help_text='Enter the skype of the theacher!', default=None),
        ),
    ]
