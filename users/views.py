from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterUserForm, LoginUserForm


def login_user(request):
     
    if request.method == 'POST':

        form = LoginUserForm(request, request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Benvido {username}', extra_tags='success')
                next = request.GET.get('next', 'home')
                return redirect(next)
        
    else:
        if 'next' in request.GET:
            messages.success(request, 'Por favor, inicia sesión antes de acceder a esa páxina.', extra_tags='danger')

        form = LoginUserForm()

    context = {'form': form}
    return render(request, 'usuarios/login.html', context)


def logout_user(request):

    logout(request)
    messages.success(request, 'Acabas de sair do sistema.', extra_tags='success')
    return redirect('home')


def register_user(request):
     
    if request.method == 'POST':

        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f'Benvido {username}', extra_tags='success')
            
            return redirect('home')
        
    else:

        form = RegisterUserForm()

    context = {'form': form}
    return render(request, 'usuarios/register_user.html', context)


