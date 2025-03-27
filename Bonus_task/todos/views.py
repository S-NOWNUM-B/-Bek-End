from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect('todo_list')

    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todos/todo_edit.html', {'form': form})

def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'todos/todo_create.html', {'form': form})

def todo_list(request):
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 5)
    title = request.GET.get('title')
    description = request.GET.get('description')
    due_date = request.GET.get('due_date')
    status = request.GET.get('status')

    todos = Todo.objects.all()

    if title:
        todos = todos.filter(title__icontains=title)
    if description:
        todos = todos.filter(description__icontains=description)
    if due_date:
        todos = todos.filter(due_date=due_date)
    if status in ["True", "False"]:
        todos = todos.filter(status=status == "True")

    paginator = Paginator(todos, page_size)
    page_obj = paginator.get_page(page)

    return render(request, 'todos/todo_list.html', {'todos': page_obj})