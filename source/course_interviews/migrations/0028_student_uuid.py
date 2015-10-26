# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0027_auto_20151023_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(null=True, blank=True, editable=False),
        ),
    ]
