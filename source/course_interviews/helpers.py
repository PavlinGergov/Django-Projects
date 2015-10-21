from .models import TeacherTimeSlot, InterviewSlot
import requests
from datetime import datetime, timedelta


class Applicant:

    def __init__(
        self, name="", email="", skype="", phone_number="", applied_course="",
        first_task="", second_task="", third_task="", studies_at="", works_at=""
    ):
        self.name = name
        self.email = email
        self.skype = skype
        self.phone_number = phone_number
        self.applied_course = applied_course
        self.first_task = first_task
        self.second_task = second_task
        self.third_task = third_task
        self.studies_at = studies_at
        self.works_at = works_at

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email.split(" ")[1][13:-1].replace("&#64;", "@")

    def get_skype(self):
        if self.skype.startswith("<a href"):
            return self.skype.split(" ")[1][13:-1].replace("&#64;", "@")
        return self.skype

    def get_phone_number(self):
        if self.phone_number.startswith('0'):
            self.phone_number = "+359" + self.phone_number[1:]
        return self.phone_number

    def get_applied_course(self):
        return self.applied_course

    def get_first_task(self):
        task = ""
        try:
            task = self.first_task.split(" ")[1][6:-1]
        except:
            pass
        return task

    def get_second_task(self):
        task = ""
        try:
            task = self.second_task.split(" ")[1][6:-1]
        except:
            pass
        return task

    def get_third_task(self):
        task = ""
        try:
            task = self.third_task.split(" ")[1][6:-1]
        except:
            pass
        return task

    def get_studies_at(self):
        return self.studies_at

    def get_works_at(self):
        return self.works_at


def get_applications(address, form_name, api_key, count, page):
    url = address + form_name + "/applications?api_key=" \
        + api_key + "&page=" + str(page) + "&count=" + str(count)
    applications = requests.get(url).json()
    return applications


def calculate_diff_in_time(start_time, end_time):
    start_delta = timedelta(
        hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
    end_delta = timedelta(
        hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second)
    return (end_delta - start_delta).seconds / 60


def generate_interview_slots(interview_time_length, break_time):
    teacher_time_slots = TeacherTimeSlot.objects.all().order_by('date')

    for slot in teacher_time_slots:
        # Check if slots are already generated
        if slot.has_generated_slots():
            continue

        free_time = calculate_diff_in_time(slot.start_time, slot.end_time)
        interview_start_time = slot.start_time

        while free_time >= interview_time_length:
            interview_slot = InterviewSlot(
                teacher_time_slot=slot,
                start_time=interview_start_time)
            interview_slot.save()

            # Decrease the free time and change the starting time of the next interview
            free_time -= (interview_time_length + break_time)
            next_interview_date_and_time = datetime.combine(
                    slot.date, interview_start_time) + timedelta(
                    minutes=(interview_time_length + break_time))
            interview_start_time = next_interview_date_and_time.time()


# def generate_interviews(interview_length):
#     students = Student.objects.all()
#     free_for_interviews = FreeForInterview.objects.all().order_by('date')
#     for student in students:

#     for x in free_for_interviews:
#         print(calculate_diff_in_time(x.start_time, x.end_time))
