from django.contrib.auth import logout,login
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView , DeleteView, CreateView,FormView
from django.utils.decorators import method_decorator
from utils.decorators import decorator_group
from .models import Task
from django.contrib.auth.views import LoginView
# Create your views here.


class LoginClass(LoginView):
    fields='__all__'
    template_name = 'base/login.html'
    redirect_authenticated_user = True
    def get_success_url(self) -> str:
        return reverse_lazy('tasks')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login'))

class RegisterClass(FormView):
    form_class = UserCreationForm
    template_name = 'base/register.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super().form_valid(form)
    
    def get(self, request: HttpRequest, *args: str, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        return super().get(request, *args, **kwargs)



@method_decorator(decorator_group(),name='dispatch')
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        search_content = self.request.GET.get('search-content') or ''
        if search_content:
            context['tasks'] = context['tasks'].filter(title__icontains=search_content)
            context['search_data'] = search_content
        return context
    
    
@method_decorator(decorator_group(),name='dispatch')
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    
    
@method_decorator(decorator_group(),name='dispatch')
class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','complete']
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)



@method_decorator(decorator_group(),name='dispatch')
class TaskUpdate(UpdateView):
    model = Task
    template_name = 'base/task_create.html'
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')


@method_decorator(decorator_group(),name='dispatch')
class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'
    template_name = 'base/task_delete.html'