from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView , DeleteView, CreateView
from .models import Task
# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'base/task_create.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'
    template_name = 'base/task_delete.html'
        