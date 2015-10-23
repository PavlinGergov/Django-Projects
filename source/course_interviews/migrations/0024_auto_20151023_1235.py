# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0023_auto_20151022_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewersFreeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='teachertimeslot',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='interviewslot',
            name='teacher_time_slot',
            field=models.ForeignKey(to='course_interviews.InterviewersFreeTime'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='interviewing_for',
            field=models.CharField(help_text='Курсът за който интервюиращият ще прави интервюта', default=False, choices=[('Programming 101 with Java', 'Programming 101 with Java'), ('Programming 101 with C#', 'Programming 101 with C#'), ('Both', 'Both')], max_length=110),
        ),
        migrations.DeleteModel(
            name='TeacherTimeSlot',
        ),
        migrations.AddField(
            model_name='interviewersfreetime',
            name='teacher',
            field=models.ForeignKey(to='course_interviews.Teacher'),
        ),
    ]
