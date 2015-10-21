from django.shortcuts import render
from django.http import JsonResponse
from .helpers import get_applications


def index(request):
    return render(request, "index.html", locals())


def get_students(request, course):
    if course == "Csharp":
        course = "Programming 101 with C#"
    elif course == "Java":
        course = "Programming 101 with Java"

    json = {
        "item": 0,
        "min": {
            "value": 0
        },
        "max": {
            "value": 0
        }
    }

    f6s_address = "https://api.f6s.com/"
    f6s_application_name = "hackbulgaria-courses-fall2015"
    f6s_api_key = "g3WHBM4UYv"
    f6s_page_count = 100
    f6s_page = 1

    while (True):
        applications = get_applications(
            f6s_address, f6s_application_name, f6s_api_key, f6s_page_count, f6s_page)
        if applications["items_count"] == 0:
            break
        f6s_page += 1
        for student in applications["data"]:
            json["max"]["value"] += 1
            if (student["status"] == "Finalized") and (
                    student["questions"][6]["field_response"][0] == course):
                json["item"] += 1

    return JsonResponse(json)
