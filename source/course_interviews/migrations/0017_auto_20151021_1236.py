# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0016_auto_20151021_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewSlots',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_time', models.TimeField(null=True)),
                ('students', models.ForeignKey(to='course_interviews.Student')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherTimeSlot',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('generated_slot', models.BooleanField(default=False)),
                ('teacher', models.ForeignKey(to='course_interviews.Teacher')),
            ],
        ),
        migrations.RemoveField(
            model_name='freeforinterview',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='FreeForInterview',
        ),
        migrations.AddField(
            model_name='interviewslots',
            name='time_slot',
            field=models.ForeignKey(to='course_interviews.TeacherTimeSlot'),
        ),
    ]
