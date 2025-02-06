from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def index(request):
    return redirect('/todo-lists')

def todo_lists(request):
    todo_lists = TodoList.objects.all()
    form = TodoListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/todo-lists')
    return render(request, 'todos/todo_lists.html', {'todo_lists': todo_lists, 'form': form})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})

def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('/todo-lists')

def todo_list_edit(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    form = TodoListForm(request.POST or None, instance=todo_list)
    if form.is_valid():
        form.save()
        return redirect(f'/todo-lists/{id}')
    return render(request, 'todos/todo_list_edit.html', {'form': form})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect(f'/todo-lists/{todo_list_id}')

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect(f'/todo-lists/{todo.todo_list.id}')
    return render(request, 'todos/todo_edit.html', {'form': form, 'todo': todo})