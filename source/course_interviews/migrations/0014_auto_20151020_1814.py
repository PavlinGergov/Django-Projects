# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0013_auto_20151020_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='skype',
            field=models.CharField(default=b'Enter valid skype for teacher', max_length=50),
        ),
    ]
