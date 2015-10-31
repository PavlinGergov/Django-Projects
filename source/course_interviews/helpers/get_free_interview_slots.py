from course_interviews.models import InterviewSlot
from datetime import datetime


def get_free_interview_slots():
    # Buffer slots are provided specially for the
    # students that can not attend their initial interview date

    # buffer_slots = InterviewSlot.objects.filter(???)  # use proper filter
    buffer_slots = []  # This variable is for testing purpose only!

    # The other slots are the ones that do not have students assigned to them
    other_slots = InterviewSlot.objects.all().order_by('teacher_time_slot__date')

    if len(buffer_slots) != 0:
        available_slots = [slot for slot
                           in buffer_slots
                           if not slot.student]
    # If no bufers are left, use other available empty slots after the current day
    else:
        today = datetime.now()
        available_slots = [slot for slot
                           in other_slots
                           if not slot.student
                           and slot.teacher_time_slot.date > datetime.date(today)]

    return available_slots
