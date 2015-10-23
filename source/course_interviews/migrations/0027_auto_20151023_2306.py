# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0026_remove_interviewslot_is_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewerFreeTime',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='interviewersfreetime',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='interviewing_for',
        ),
        migrations.AlterField(
            model_name='interviewslot',
            name='teacher_time_slot',
            field=models.ForeignKey(to='course_interviews.InterviewerFreeTime'),
        ),
        migrations.DeleteModel(
            name='InterviewersFreeTime',
        ),
        migrations.AddField(
            model_name='interviewerfreetime',
            name='teacher',
            field=models.ForeignKey(to='course_interviews.Teacher'),
        ),
    ]
