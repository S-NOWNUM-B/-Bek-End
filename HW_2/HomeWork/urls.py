from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import StudentViewSet, CourseViewSet
from .views import student_list, course_list, index

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", index, name="index"),
    path("students/", student_list, name="students"),
    path("courses/", course_list, name="courses"),
]