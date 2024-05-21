from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, ContactDataForm
from store.models import User, ContactData
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('personal_area'))

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
    if request.method == 'POST':
        form = ContactDataForm(request.POST)

        if form.is_valid():
            new_contact_data = ContactData.objects.create(
                user=request.user,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone']
            )

            new_contact_data.save()

            return redirect(reverse('personal_area'))

    return render(
        request=request,
        template_name='personal_area/personal_area.html',
        context={'contact_data_form': ContactDataForm()}
    )


@login_required
def logout(request):
    django_logout(request)
    return redirect(reverse('login'))


@login_required
def products(request):
    return render(
        request=request,
        template_name='personal_area/products.html',
        context={}
     )


@login_required
def storages(request):
    return redirect(reverse('personal_area'))

