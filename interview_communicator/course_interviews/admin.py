from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Student, Teacher, FreeForInterview


# class SuccessStoryPersonAdmin(SortableAdminMixin, admin.ModelAdmin):
#     pass
# admin.site.register(SuccessStoryPerson, SuccessStoryPersonAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)


class FreeForInterviewAdmin(admin.ModelAdmin):
    model = FreeForInterview

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        return queryset.filter(teacher=request.user.teacher)

admin.site.register(FreeForInterview, FreeForInterviewAdmin)


# class TeacherAdmin(admin.ModelAdmin):
#     inlines = [FreeForInterviewInline, ]
# admin.site.register(Teacher, TeacherAdmin)


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (TeacherInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
