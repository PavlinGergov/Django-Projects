# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0014_auto_20151020_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='skype',
            field=models.CharField(default=None, help_text=b'Enter the skype of the theacher!', max_length=50),
        ),
    ]
