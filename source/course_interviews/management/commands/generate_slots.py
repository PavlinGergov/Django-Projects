from django.core.management.base import BaseCommand
from course_interviews.helpers import GenerateInterviewSlots


class Command(BaseCommand):
    help = 'Make a request to f6s and add applicants with finalized forms'

    def handle(self, **options):
        interview_length = 30
        break_between_interviews = 10

        interview_slots_generator = GenerateInterviewSlots(
            interview_length, break_between_interviews)

        interview_slots_generator.generate_interview_slots()
        generated_slots = interview_slots_generator.get_generated_slots()

        print(str(generated_slots) + ' slots were generated')
