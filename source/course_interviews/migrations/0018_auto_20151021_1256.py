# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0017_auto_20151021_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('start_time', models.TimeField(null=True)),
                ('student', models.ForeignKey(null=True, to='course_interviews.Student')),
                ('time_slot', models.ForeignKey(to='course_interviews.TeacherTimeSlot')),
            ],
        ),
        migrations.RemoveField(
            model_name='interviewslots',
            name='students',
        ),
        migrations.RemoveField(
            model_name='interviewslots',
            name='time_slot',
        ),
        migrations.DeleteModel(
            name='InterviewSlots',
        ),
    ]
