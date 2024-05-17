from django.shortcuts import render
from .forms import LoginForm, RegisterForm


def login(request):
    return render(
        request=request,
        template_name='personal_area/login.html',
        context={
            'form': LoginForm()
        }
    )


def register(request):
    return render(
        request=request,
        template_name='personal_area/register.html',
        context={
            'form': RegisterForm()
        }
    )
