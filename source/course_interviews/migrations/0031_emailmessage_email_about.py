# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0030_emailmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='email_about',
            field=models.CharField(null=True, help_text="What's the email about?", max_length=50),
        ),
    ]
