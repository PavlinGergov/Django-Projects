# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_interviews', '0004_auto_20151015_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
