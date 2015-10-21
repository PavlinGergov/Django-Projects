# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_interviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeForInterview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('skype', models.CharField(max_length=50, default=False)),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='skype',
            field=models.CharField(max_length=50, default=False),
        ),
        migrations.AddField(
            model_name='freeforinterview',
            name='teacher',
            field=models.ForeignKey(to='course_interviews.Teacher'),
        ),
    ]
