from django.contrib import admin
from django.urls import path, include
from todos.views import todo_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
    path('', todo_list, name='home'),
]