# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0010_auto_20151017_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='code_skills_rating',
            field=models.IntegerField(default=0, max_length=10, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
        migrations.AddField(
            model_name='student',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
