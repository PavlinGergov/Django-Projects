from django.core.management.base import BaseCommand
from course_interviews.models import Student
from course_interviews.helpers import Applicant, get_applications


class Command(BaseCommand):
    help = 'Make a request to f6s and add applicants with finalized forms'

    def handle(self, **options):
        f6s_address = "https://api.f6s.com/"
        f6s_application_name = "hackbulgaria-courses-fall2015"
        f6s_api_key = "g3WHBM4UYv"
        f6s_page_count = 100
        f6s_page = 1

        errors = 0
        while (True):
            applications = get_applications(
                f6s_address, f6s_application_name, f6s_api_key, f6s_page_count, f6s_page)
            if applications["items_count"] == 0:
                break
            f6s_page += 1

            for person in applications["data"]:
                if person["status"] == "Finalized":
                    applicant = Applicant(
                        name=person["questions"][0]["question_response"],
                        studies_at=person["questions"][1]["question_response"],
                        works_at=person["questions"][2]["question_response"],
                        first_task=person["questions"][3]["question_response"],
                        second_task=person["questions"][4]["question_response"],
                        third_task=person["questions"][5]["question_response"],
                        applied_course=person["questions"][6]["field_response"][0],
                        email=person["questions"][7]["question_response"],
                        skype=person["questions"][8]["question_response"],
                        phone_number=person["questions"][9]["question_response"],
                    )
                    student = Student(
                        name=applicant.get_name(),
                        studies_at=applicant.get_studies_at(),
                        works_at=applicant.get_works_at(),
                        first_task=applicant.get_first_task(),
                        second_task=applicant.get_second_task(),
                        third_task=applicant.get_third_task(),
                        applied_course=applicant.get_applied_course(),
                        email=applicant.get_email(),
                        skype=applicant.get_skype(),
                        phone_number=applicant.get_phone_number(),
                    )
                    try:
                        student.save()
                    except Exception:
                        errors += 1
                        # TODO: handle?
                        pass
        print(str(errors) + ' errors occured.')
