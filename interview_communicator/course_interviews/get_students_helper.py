import requests


class Applicant:

    def __init__(
        self, name, email, skype, phone_number, applied_course,
        first_task, second_task, third_task, studies_at, works_at
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
        pass

    def get_email(self):
        pass

    def get_skype(self):
        pass

    def get_phone_number(self):
        pass

    def get_applied_course(self):
        pass

    def get_first_task(self):
        pass

    def get_second_task(self):
        pass

    def get_third_task(self):
        pass

    def get_studies_at(self):
        pass

    def get_works_at(self):
        pass


class GetApplicants:
    ADDRESS = "https://api.f6s.com/"

    def __init__(self, form_name, api_key):
        self.form_name = form_name
        self.api_key = api_key
        self.students = None

    def get_all_students(self):
        url = self.ADDRESS + self.form_name + "/applications?api_key=" + self.api_key
        form_data = requests.get(url).json()["data"]


# applicants = GetApplicants("hackbulgaria-courses-fall2015", "g3WHBM4UYv")
