from django.urls import path
from .views import todo_list, todo_create, todo_edit, todo_delete

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('<int:pk>/edit/', todo_edit, name='todo_edit'),
    path('<int:pk>/delete/', todo_delete, name='todo_delete'),
]