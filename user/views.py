from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from user.forms import UserRegisterForm
from user.models import User


def user_register_view(request):
    if request.user.is_authenticated:
        return redirect(to='ecommerce:home')

    register_form = UserRegisterForm()

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()

    return render(request, 'user/register.html', {
        'register_form': register_form
    })


def user_login_view(request):
    if request.user.is_authenticated:
        return redirect(to='ecommerce:home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('ecommerce:home')

    return render(request, 'user/login.html')


def user_logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('user_login')
