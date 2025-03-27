from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status', 'todo_list']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'todo_list': forms.Select(),
        }