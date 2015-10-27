# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0033_auto_20151027_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='has_email',
            new_name='has_received_email',
        ),
    ]
