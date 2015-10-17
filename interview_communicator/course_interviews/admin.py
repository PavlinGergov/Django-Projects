from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Student, Teacher, FreeForInterview


class StudentAdmin(admin.ModelAdmin):
        list_display = [
            'name',
            'email',
            'skype',
            'phone_number',
            'applied_course',
            'has_been_interviewed',
            'teacher_comment'
        ]
        list_filter = ['applied_course', 'has_been_interviewed']
        search_fields = ['name', 'email', 'skype']

admin.site.register(Student, StudentAdmin)


class FreeForInterviewAdmin(admin.ModelAdmin):
    model = FreeForInterview

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.user = request.user
    #     obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(teacher=request.user.teacher)

admin.site.register(FreeForInterview, FreeForInterviewAdmin)


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (TeacherInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
