from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroUserFrom

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Bienvenido!')
            return redirect('home')
        else:
            messages.success(request, 'Algo fue mal... Intenta Nuevamente!')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Cerraste Session.. Hasta Luego!')
    return redirect('login')

def registrar(request):
    if request.method == 'POST':
        form = RegistroUserFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registro Completado!')
            return redirect('home')
    else:
        form = RegistroUserFrom()
    return render(request, 'authenticate/registro.html', {'form':form})
