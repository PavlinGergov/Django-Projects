# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('applied_course', models.CharField(max_length=110, null=True, blank=True)),
                ('first_task', models.URLField(null=True, blank=True)),
                ('second_task', models.URLField(null=True, blank=True)),
                ('third_task', models.URLField(null=True, blank=True)),
                ('studies_at', models.CharField(max_length=110, null=True, blank=True)),
                ('works_at', models.CharField(max_length=110, null=True, blank=True)),
                ('phone_number', models.CharField(max_length='20', null=True, blank=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('has_interview_date', models.BooleanField(default=False)),
                ('has_been_interviewd', models.BooleanField(default=False)),
            ],
        ),
    ]
