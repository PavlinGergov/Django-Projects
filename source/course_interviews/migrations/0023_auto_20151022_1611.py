# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0022_student_has_confirmed_interview'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='interviewing_for',
            field=models.CharField(help_text='Курсът за който интервюиращият ще прави интервюта', default=False, max_length=110, choices=[(0, 'Programming 101 with Java'), (0, 'Programming 101 with C#')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='skype',
            field=models.CharField(help_text='Enter the skype of the teacher!', default=None, max_length=50),
        ),
    ]
