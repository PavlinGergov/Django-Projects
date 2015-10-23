from .models import Student, InterviewersFreeTime, InterviewSlot
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


class GetStudents:

    def __init__(self, address, form_name, api_key, count, page):
        self.address = address
        self.form_name = form_name
        self.api_key = api_key
        self.count = count
        self.page = page

    def get_student_applications(self):
        url = self.address + self.form_name + "/applications?api_key=" \
            + self.api_key + "&page=" + str(self.page) + "&count=" + str(self.count)
        applications = requests.get(url).json()
        return applications


class CourseStudents(GetStudents):

    def __init__(self, address, form_name, api_key, count, page, course):
        super().__init__(address, form_name, api_key, count, page)
        self.course = course
        self.__json = {
            "item": 0,
            "min": {
                "value": 0
            },
            "max": {
                "value": 0
            }
        }

    def generate_students_for_course(self):
        while (True):
            applications = self.get_student_applications()
            if applications["items_count"] == 0:
                break

            # Break loop if all students are added
            self.page += 1
            for student in applications["data"]:
                if student["questions"][6]["field_response"] and \
                        student["questions"][6]["field_response"][0] == self.course:
                    self.__json["max"]["value"] += 1
                    if student["status"] == "Finalized":
                        self.__json["item"] += 1

    def get_json(self):
        return self.__json


class GenerateStudents(GetStudents):

    def __init__(self, address, form_name, api_key, count, page):
        super().__init__(address, form_name, api_key, count, page)
        self.__errors = 0

    def __inc_errors(self):
        self.__errors += 1

    def __add_applicant(self, person):
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
                self.__inc_errors()
                # TODO: handle?
                pass

    def generate_students(self):
        while (True):
            applications = self.get_student_applications()

            # Break loop if all students are added
            if applications["items_count"] == 0:
                break

            self.page += 1
            for person in applications["data"]:
                self.__add_applicant(person)

    def get_errors(self):
        return self.__errors


class GenerateInterviewSlots:

    def __init__(self, interview_time_length, break_time):
        self.interview_time_length = interview_time_length
        self.break_time = break_time
        self.__slots_generated = 0

    def __inc_slots_generated(self):
        self.__slots_generated += 1

    def __calculate_diff_in_time(self, start_time, end_time):
        start_delta = timedelta(
            hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
        end_delta = timedelta(
            hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second)
        return (end_delta - start_delta).seconds / 60

    def generate_interview_slots(self):
        teacher_time_slots = InterviewersFreeTime.objects.all().order_by('date')

        for slot in teacher_time_slots:
            # Check if slots are already generated
            if slot.has_generated_slots():
                continue

            free_time = self.__calculate_diff_in_time(slot.start_time, slot.end_time)
            interview_start_time = slot.start_time

            while free_time >= self.interview_time_length:
                interview_slot = InterviewSlot(
                    teacher_time_slot=slot,
                    start_time=interview_start_time)
                interview_slot.save()

                self.__inc_slots_generated()

                # Decrease the free time and change the starting time of the next interview
                free_time -= (self.interview_time_length + self.break_time)
                next_interview_date_and_time = datetime.combine(
                        slot.date, interview_start_time) + timedelta(
                        minutes=(self.interview_time_length + self.break_time))
                interview_start_time = next_interview_date_and_time.time()

    def get_generated_slots(self):
        return self.__slots_generated


class GenerateInterviews:

    def __init__(self):
        self.__students_without_interviews = 0
        self.__generated_interviews = 0

    def __set_students_without_interviews(self, students):
        self.__students_without_interviews = len(students)

    def __inc_generated_interviews(self):
        self.__generated_interviews += 1

    def generate_interviews(self):
        students = list(Student.objects.all())
        slots = InterviewSlot.objects.all()
        for slot in slots:
            if len(students) != 0:
                student = students.pop(0)
                if not student.has_interview_date:
                    self.__inc_generated_interviews()
                    slot.student = student
                    student.has_interview_date = True
                    slot.save()
                    student.save()
            else:
                break
        self.__set_students_without_interviews(students)

    def get_students_without_interviews(self):
        return self.__students_without_interviews

    def get_generated_interviews_count(self):
        return self.__generated_interviews
