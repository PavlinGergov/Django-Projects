# -*- coding: utf-8 -*-
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    skype = models.CharField(default=None, max_length=110)
    phone_number = PhoneNumberField(blank=True)
    applied_course = models.CharField(null=True, blank=True, max_length=110)
    first_task = models.URLField(null=True, blank=True)
    second_task = models.URLField(null=True, blank=True)
    third_task = models.URLField(null=True, blank=True)
    studies_at = models.CharField(blank=True, null=True, max_length=110)
    works_at = models.CharField(null=True, blank=True, max_length=110)
    # possible_rating is number between 1 and 10 to be selected in the integer field
    possible_ratings = [(i, i) for i in range(11)]
    code_skills_rating = models.IntegerField(
        default=0,
        choices=possible_ratings,
        help_text='Оценка върху уменията на кандидата да пише'
        ' код и знанията му върху базови алгоритми')
    code_design_rating = models.IntegerField(
        default=0,
        choices=possible_ratings,
        help_text='Оценка върху уменията на кандидата да "съставя'
        ' програми" и да разбива нещата по парчета + базово OOP')
    fit_attitude_rating = models.IntegerField(
        default=0,
        choices=possible_ratings,
        help_text='Оценка на интервюиращия в зависимост от'
        ' усета му за човека (става ли за курса)')
    teacher_comment = models.TextField(
        null=True,
        blank=True,
        help_text='Коментар на интервюиращия за цялостното представяне на кандидата')
    has_interview_date = models.BooleanField(default=False)
    has_confirmed_interview = models.BooleanField(default=False)
    has_been_interviewed = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User)
    skype = models.CharField(
        default=None,
        max_length=50,
        help_text='Enter the skype of the theacher!')

    def __str__(self):
        return self.user.get_full_name()


class TeacherTimeSlot(models.Model):
    teacher = models.ForeignKey(Teacher)
    date = models.DateField(blank=False, null=True)
    start_time = models.TimeField(blank=False, null=True)
    end_time = models.TimeField(blank=False, null=True)

    def has_generated_slots(self):
        return self.interviewslot_set.exists()

    def __str__(self):
        return str(self.date) + " - from " + str(self.start_time) + " to " + str(self.end_time)


class InterviewSlot(models.Model):
    teacher_time_slot = models.ForeignKey(TeacherTimeSlot)
    student = models.ForeignKey(Student, null=True)
    start_time = models.TimeField(blank=False, null=True)
