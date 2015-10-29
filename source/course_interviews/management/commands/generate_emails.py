from django.core.management.base import BaseCommand
from course_interviews.models import Student
from post_office import mail


class Command(BaseCommand):
    help = 'Generate emails for interview date confirmation'

    def handle(self, **options):

        recipients = [student for student in Student.objects.filter(has_received_email=False)]
        template = 'interview_confirmation'

        for student in recipients:
            mail.send(
                recipients=[student.email],
                template=template,
                context={
                    'name': student.name,
                    'applied_course': student.applied_course,
                    'token': student.uuid
                })
            student.has_received_email = True
            student.save()
