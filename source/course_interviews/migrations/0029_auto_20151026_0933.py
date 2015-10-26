# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0028_student_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(unique=True, editable=False, default=uuid.uuid4, blank=True),
        ),
    ]
