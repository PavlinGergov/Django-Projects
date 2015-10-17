from django.core.management.base import BaseCommand
from course_interviews.models import Student
import requests


class Command(BaseCommand):
    help = 'Make a request to f6s and add students with finalized forms'

    def handle(self, **options):
        print("I made a custom command panda")
