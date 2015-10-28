from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import Student, InterviewSlot
from .helpers.course_students import CourseStudents
from .helpers.get_students_emails import GetStudentsEmails
from .helpers.get_free_interview_slots import get_free_interview_slots


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


def get_emails(request):
    courses = ["Programming 101 with C#", "Programming 101 with Java"]

    f6s_address = "https://api.f6s.com/"
    f6s_application_name = "hackbulgaria-courses-fall2015"
    f6s_api_key = "g3WHBM4UYv"
    f6s_page_count = 100
    f6s_page = 1

    get_students_emails_generator = GetStudentsEmails(
        f6s_address, f6s_application_name, f6s_api_key, f6s_page_count, f6s_page, courses)

    get_students_emails_generator.generate_students_emails()
    json = get_students_emails_generator.get_json()

    return JsonResponse(json)


def get_interview_slots(request):
    json = []
    available_slots = get_free_interview_slots()

    for slot in available_slots:
        json.append({
            "date": slot.teacher_time_slot.date,
            "time": slot.start_time,
            "slot_id": slot.id
            })

    return JsonResponse(json, safe=False)


def confirm_interview(request, token):
    student = get_object_or_404(Student, uuid=token)

    if student.has_confirmed_interview:
        return render(request, "already_confirmed_interview.html", locals())

    elif not student.has_interview_date:
        return HttpResponseNotFound('<h1>You do not have an interview date!</h1>')

    student.has_confirmed_interview = True
    student.save()
    return render(request, "confirm_interview.html", locals())


def choose_interview(request, token):
    student = get_object_or_404(Student, uuid=token)

    # If student has interview_date, he should't see the page
    if student.has_interview_date:
        return HttpResponseNotFound('<h1>You already have an interview!</h1>')

    available_slots = get_free_interview_slots()

    return render(request, "choose_interview.html", locals())


def confirm_slot(request):
    slot_id = request.POST["slot_id"]
    student_uuid = request.POST["student_uuid"]

    slot = get_object_or_404(InterviewSlot, id=slot_id)
    student = get_object_or_404(Student, uuid=student_uuid)

    if slot.student:
        return HttpResponseNotFound("The interview is already taken!")

    # Make sure the auto generated slot the student already has is gona be free
    try:
        vacate_slot = InterviewSlot.objects.filter(student=student)
        vacate_slot = vacate_slot[0]
        vacate_slot.student = None
        vacate_slot.save()
    except:
        pass

    slot.student = student
    student.has_interview_date = True

    slot.save()
    student.save()

    return HttpResponse("OK")
