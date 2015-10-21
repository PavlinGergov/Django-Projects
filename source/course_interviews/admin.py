from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Student, Teacher, FreeForInterview


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


class FreeForInterviewAdmin(admin.ModelAdmin):
    model = FreeForInterview

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude = ['teacher']
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.teacher = request.user.teacher
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(teacher=request.user.teacher)

    # readonly_fields = ('teacher', )
    list_display = [
        "teacher",
        "date",
        "start_time",
        "end_time"
    ]
    list_filter = ["date", "start_time", "end_time"]
    search_fields = ["teacher"]

admin.site.register(FreeForInterview, FreeForInterviewAdmin)


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (TeacherInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
