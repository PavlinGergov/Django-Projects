# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0006_remove_teacher_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='has_been_interviewd',
            new_name='has_been_interviewed',
        ),
    ]
