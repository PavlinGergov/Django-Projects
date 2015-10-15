from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    skype = models.CharField(default=None, max_length=50)
    applied_course = models.CharField(null=True, blank=True, max_length=110)
    first_task = models.URLField(null=True, blank=True)
    second_task = models.URLField(null=True, blank=True)
    third_task = models.URLField(null=True, blank=True)
    studies_at = models.CharField(blank=True, null=True, max_length=110)
    works_at = models.CharField(null=True, blank=True, max_length=110)
    phone_number = models.CharField(null=True, blank=True, max_length='20')
    email = models.EmailField(unique=True)
    has_interview_date = models.BooleanField(default=False)
    has_been_interviewd = models.BooleanField(default=False)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    skype = models.CharField(default=None, max_length=50)
    email = models.EmailField(unique=True)


class FreeForInterview(models.Model):
    teacher = models.ForeignKey(Teacher)
    name = models.CharField(max_length=50)
    # date = datetime
    # start_time = time
    # end_time = time
