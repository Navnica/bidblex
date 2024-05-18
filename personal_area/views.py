from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                django_login(request, user)
                return redirect('personal_area')
            else:
                return render(
                    request=request,
                    template_name='personal_area/login.html',
                    context={
                        'form': form,
                        'error': 'Неверное имя пользователя или пароль'
                    }
                )
    else:
        form = LoginForm()

    return render(
        request=request,
        template_name='personal_area/login.html',
        context={
            'form': form
        }
    )


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            try:
                new_user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )

                new_user.save()
                return redirect('login')

            except IntegrityError:
                return render(
                    request=request,
                    template_name='personal_area/register.html',
                    context={
                        'form': form,
                        'error': 'Имя пользователя или email уже используется'
                    }
                )

    return render(
        request=request,
        template_name='personal_area/register.html',
        context={
            'form': RegisterForm()
        }
    )


@login_required
def personal_area(request):
    return HttpResponse(request.user.username)
