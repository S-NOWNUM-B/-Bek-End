from django.shortcuts import render
from .students.models import Student
from .subjects.models import Course

def student_list(request):
    students = Student.objects.all()
    return render(request, "student-list.html", {"students": students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses_list.html", {"courses": courses})

def index(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, "index.html", {"students": students, "courses": courses})