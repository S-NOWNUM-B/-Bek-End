from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('todo_lists')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_lists')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'user/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('todo_lists')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Пароли не совпадают.')
            return render(request, 'user/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует.')
            return render(request, 'user/register.html')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect('todo_lists')

    return render(request, 'user/register.html')