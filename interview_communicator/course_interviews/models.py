from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    skype = models.CharField(default=None, max_length=50)
    phone_number = PhoneNumberField(blank=True)
    applied_course = models.CharField(null=True, blank=True, max_length=110)
    first_task = models.URLField(null=True, blank=True)
    second_task = models.URLField(null=True, blank=True)
    third_task = models.URLField(null=True, blank=True)
    studies_at = models.CharField(blank=True, null=True, max_length=110)
    works_at = models.CharField(null=True, blank=True, max_length=110)
    teacher_comment = models.TextField(null=True, blank=True)
    has_interview_date = models.BooleanField(default=False)
    has_been_interviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User)
    skype = models.CharField(default=None, max_length=50)

    def __str__(self):
        return self.user.get_full_name()


class FreeForInterview(models.Model):
    teacher = models.ForeignKey(Teacher)
    date = models.DateField(blank=False, null=True)
    start_time = models.TimeField(blank=False, null=True)
    end_time = models.TimeField(blank=False, null=True)

    def __str__(self):
        return str(self.date) + " - from " + str(self.start_time) + " to " + str(self.end_time)

    # date = datetime
    # start_time = time
    # end_time = time
