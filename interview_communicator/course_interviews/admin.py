from django.contrib import admin

# from adminsortable2.admin import SortableAdminMixin
from .models import Student, Teacher, FreeForInterview


# class SuccessStoryPersonAdmin(SortableAdminMixin, admin.ModelAdmin):
#     pass
# admin.site.register(SuccessStoryPerson, SuccessStoryPersonAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)


class FreeForInterviewInline(admin.StackedInline):
    model = FreeForInterview
    extra = 1


class TeacherAdmin(admin.ModelAdmin):
    inlines = [FreeForInterviewInline, ]
admin.site.register(Teacher, TeacherAdmin)
