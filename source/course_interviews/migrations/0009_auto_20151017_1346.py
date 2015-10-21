# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0008_student_teacher_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freeforinterview',
            name='name',
        ),
        migrations.AddField(
            model_name='freeforinterview',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='freeforinterview',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='freeforinterview',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
