# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0024_auto_20151023_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewslot',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
