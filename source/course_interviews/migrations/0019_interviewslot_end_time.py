# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0018_auto_20151021_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewslot',
            name='end_time',
            field=models.TimeField(null=True),
        ),
    ]
