from django.shortcuts import render
from .forms import LoginForm


def login(request):
    return render(request, 'personal_area/login.html', {'login_form': LoginForm()})
