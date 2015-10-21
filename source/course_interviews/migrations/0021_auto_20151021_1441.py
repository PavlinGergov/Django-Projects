# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0020_remove_interviewslot_end_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviewslot',
            old_name='time_slot',
            new_name='teacher_time_slot',
        ),
        migrations.RemoveField(
            model_name='teachertimeslot',
            name='generated_slot',
        ),
    ]
