from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse


def login(request):
    return render(request, 'personal_area/login.html', {'login_form': LoginForm()})


def register(request):
    return HttpResponse('<center>Здесь будет регистрация</center>')