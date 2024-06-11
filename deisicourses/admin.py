from django.contrib import admin
from .models import Teacher, Course, Branch, Programming_Language, CurricularUnit, Project


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'director__name',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Programming_Language)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CurricularUnit)
class CurricularUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'semester', 'ects', 'cu_readable_code', 'time_spent',)
    filter_horizontal = ('teachers',)  # Update filter_horizontal as needed.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',)
