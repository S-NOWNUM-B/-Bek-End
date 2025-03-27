from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

@login_required
def redirect_to_todo_lists(request):
    return redirect('todo_lists')

@login_required
def todo_lists(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            TodoList.objects.create(title=title, description=description, user=request.user)
        return redirect('todo_lists')

    lists = TodoList.objects.filter(user=request.user)
    return render(request, 'todos/todo_lists.html', {'lists': lists})

@login_required
def todo_list_detail(request, list_id):
    todo_list = get_object_or_404(TodoList, id=list_id, user=request.user)
    todo_lists = TodoList.objects.filter(user=request.user)

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect('todo_list_detail', list_id=list_id)
    else:
        form = TodoForm()

    return render(request, 'todos/todo_list_detail.html', {
        'todo_list': todo_list,
        'todo_lists': todo_lists,
        'form': form
    })

@login_required
def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id, user=request.user)
    todo_list.delete()
    return redirect('todo_lists')

@login_required
def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id, user=request.user)
    if request.method == 'POST':
        todo_list.title = request.POST.get('title', todo_list.title)
        todo_list.description = request.POST.get('description', todo_list.description)
        todo_list.save()
        return redirect('todo_list_detail', list_id=todo_list.id)

    return render(request, 'todos/edit_todo_list.html', {'todo_list': todo_list})

@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, todo_list__user=request.user)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', list_id=todo_list_id)

@login_required
def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id, todo_list__user=request.user)
    todo_lists = TodoList.objects.filter(user=request.user)

    if request.method == 'POST':
        todo.title = request.POST.get('title', todo.title)
        todo.description = request.POST.get('description', todo.description)
        todo.due_date = request.POST.get('due_date', todo.due_date)
        todo.status = request.POST.get('status') == 'on'

        new_list_id = request.POST.get('todo_list')
        if new_list_id and new_list_id != str(todo.todo_list.id):
            new_list = get_object_or_404(TodoList, id=new_list_id, user=request.user)
            todo.todo_list = new_list

        todo.save()
        return redirect('todo_list_detail', list_id=todo.todo_list.id)

    return render(request, 'todos/edit_todo.html', {'todo': todo, 'todo_lists': todo_lists})