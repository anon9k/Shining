from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterUserForm, LoginUserForm

#método de registro de un nuevo usuario, en caso de registrarse correctamente
# se loguea con ese usuario y se redirige a home
def register_user(request):
     
    if request.method == 'POST':

        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f'Bienvenido {username}', extra_tags='success')
            
            return redirect('home')
        
    else:

        form = RegisterUserForm()

    context = {'form': form}
    return render(request, 'users/register_user.html', context)

#método login
def login_user(request):
     
    if request.method == 'POST':

        form = LoginUserForm(request, request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {username}', extra_tags='success')
                #en caso de acceder a algo que requiere autentificación, se pedirá un logeo y al logearse, 
                #gracias next se redirige a la pagina a la que se trataba de acceder
                next = request.GET.get('next', 'home')
                return redirect(next)
        
    else:
        if 'next' in request.GET:
            messages.success(request, 'Por favor, inicia sesión antes de acceder a esta página.', extra_tags='danger')

        form = LoginUserForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)

#método de logout que redirige a home
def logout_user(request):

    logout(request)
    messages.success(request, 'Acabas de cerrar sesión', extra_tags='success')
    return redirect('home')