# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0007_auto_20151017_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
