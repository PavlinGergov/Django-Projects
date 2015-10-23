# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0025_interviewslot_is_taken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewslot',
            name='is_taken',
        ),
    ]
