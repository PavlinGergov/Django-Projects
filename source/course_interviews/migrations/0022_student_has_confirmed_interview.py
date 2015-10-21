# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0021_auto_20151021_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='has_confirmed_interview',
            field=models.BooleanField(default=False),
        ),
    ]
