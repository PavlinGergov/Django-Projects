from django.core.management.base import BaseCommand
from course_interviews.helpers import generate_interview_slots


class Command(BaseCommand):
    help = 'Make a request to f6s and add applicants with finalized forms'

    def handle(self, **options):
        generate_interview_slots(20, 5)
