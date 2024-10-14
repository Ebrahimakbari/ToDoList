from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView , DeleteView, CreateView
from .models import Task

from django.contrib.auth.views import LoginView
# Create your views here.

logout
class LoginClass(LoginView):
    fields='__all__'
    template_name = 'base/login.html'
    redirect_authenticated_user = True
    def get_success_url(self) -> str:
        return reverse_lazy('tasks')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login'))


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