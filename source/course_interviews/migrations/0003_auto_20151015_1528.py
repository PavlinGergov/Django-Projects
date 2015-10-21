# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0002_auto_20151015_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=None, max_length='20'),
        ),
        migrations.AlterField(
            model_name='student',
            name='skype',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='skype',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
