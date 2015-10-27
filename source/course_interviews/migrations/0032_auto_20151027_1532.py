# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0031_emailmessage_email_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='email_about',
            field=models.CharField(default='', help_text="What's the email about?", max_length=50),
        ),
    ]
