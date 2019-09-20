# Python bytecode 3.7 (3394)
# Embedded file name: E:\AMKP\amkp\accounts\views.py
# Size of source mod 2**32: 2805 bytes
# Decompiled by https://python-decompiler.com
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        username = email
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(
                    request, 'Cet adresse email a déjà été utilisée')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.success(
                    request, 'Votre compte a été créer, vous pouvez maintenant vous connectez')
                return redirect('login')
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Identifiants invalides')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Vous êtes maintenant deconnecté')
        return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def publications(request):
    return render(request, 'accounts/publications.html')


def add_publication(request):
    return render(request, 'accounts/add_publication.html')
