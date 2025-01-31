from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import StudentViewSet, CourseViewSet  # Импорт API-контроллеров

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Добавляем маршруты API
]