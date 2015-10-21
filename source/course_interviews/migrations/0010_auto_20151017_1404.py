# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0009_auto_20151017_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freeforinterview',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='freeforinterview',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='freeforinterview',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
