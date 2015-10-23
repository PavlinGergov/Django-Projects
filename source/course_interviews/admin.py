from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Student, Teacher, InterviewersFreeTime, InterviewSlot


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        # 'email',
        # 'skype',
        # 'phone_number',
        'applied_course',
        'code_skills_rating',
        'code_design_rating',
        'fit_attitude_rating',
        'has_interview_date',
        'has_been_interviewed',
        'is_accepted'
    ]
    list_filter = [
        'applied_course',
        'code_skills_rating',
        'code_design_rating',
        'fit_attitude_rating',
        'has_been_interviewed',
        'is_accepted'
    ]
    search_fields = ['name', 'email', 'skype']

admin.site.register(Student, StudentAdmin)


class InterviewersFreeTimeAdmin(admin.ModelAdmin):
    model = InterviewersFreeTime

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude = ['teacher']
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change and not request.user.is_superuser:
            obj.teacher = request.user.teacher
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(teacher=request.user.teacher)

    list_display = [
        "teacher",
        "date",
        "start_time",
        "end_time"
    ]
    list_filter = ["date", "start_time", "end_time"]
    search_fields = ["teacher"]

admin.site.register(InterviewersFreeTime, InterviewersFreeTimeAdmin)


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (TeacherInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class InterviewSlotAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(
            teacher_time_slot=request.user.teacher.interviewersfreetime_set.all())

    def get_date(self, obj):
        return obj.teacher_time_slot.date
    get_date.short_description = 'Date'
    get_date.admin_order_field = 'teacher_time_slot__date'

    def get_start_time(self, obj):
        return obj.start_time
    get_start_time.short_description = "Starting"
    get_start_time.admin_order_field = 'start_time'

    def get_student(self, obj):
        if obj.student_id and obj.student.name:
            return u"<a href='../student/{0}/'>{1}</a>".format(obj.student_id, obj.student.name)
        return
    get_student.short_description = "Student"
    get_student.allow_tags = True

    def get_teacher(self, obj):
        return obj.teacher_time_slot.teacher
    get_teacher.short_description = "Teacher"

    list_display = [
        'get_date',
        'get_start_time',
        'get_student',
        'get_teacher',
    ]

admin.site.register(InterviewSlot, InterviewSlotAdmin)
