import requests


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


class GetApplicants:

    def __init__(self, address, form_name, api_key):
        self.address = address
        self.form_name = form_name
        self.api_key = api_key

    def get_all_applicants(self):
        url = self.address + self.form_name + "/applications?api_key=" + self.api_key
        form_data = requests.get(url).json()["data"]
        return form_data


def get_applications(address, form_name, api_key, count, page):
    url = address + form_name + "/applications?api_key=" \
        + api_key + "&page=" + str(page) + "&count=" + str(count)
    applications = requests.get(url).json()
    return applications
