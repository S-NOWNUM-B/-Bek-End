from django.contrib import admin
from .students.models import Student
from .subjects.models import Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "major", "year_of_study", "faculty")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "author")