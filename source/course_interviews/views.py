from django.shortcuts import render
from django.http import JsonResponse
from .helpers import CourseStudents


def index(request):
    return render(request, "index.html", locals())


def get_students(request, course):
    if course == "Csharp":
        course = "Programming 101 with C#"
    elif course == "Java":
        course = "Programming 101 with Java"

    f6s_address = "https://api.f6s.com/"
    f6s_application_name = "hackbulgaria-courses-fall2015"
    f6s_api_key = "g3WHBM4UYv"
    f6s_page_count = 100
    f6s_page = 1

    course_students_generator = CourseStudents(
        f6s_address, f6s_application_name, f6s_api_key, f6s_page_count, f6s_page, course)

    course_students_generator.generate_students_for_course()
    json = course_students_generator.get_json()

    return JsonResponse(json)
