# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0032_auto_20151027_1532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailMessage',
        ),
        migrations.AddField(
            model_name='student',
            name='has_email',
            field=models.BooleanField(default=False),
        ),
    ]
