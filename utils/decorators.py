from django.shortcuts import redirect
from django.urls import reverse_lazy


def decorator_group(data=None):
    def decorator_func(func):
        def wrapper(request,*args, **kwargs):
            if request.user.is_authenticated:
                return func(request,*args, **kwargs)
            else:
                return redirect(reverse_lazy('login'))
        return wrapper
    return decorator_func