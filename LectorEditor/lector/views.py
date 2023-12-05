from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroForm, EmailForm

def Home(request):
    return render(request, 'home.html')

def SignUp(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Signin')
    else:
        form = RegistroForm()

    return render(request, 'signup.html', {'form': form})

def SignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Editor')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'signin.html')

def LogOut(request):
    logout(request)
    return redirect('Home')

def ResetPass(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            return redirect('Setpass', user_id=user.id)
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe')
    else:
        form = EmailForm()
    return render(request, 'pass.html', {'form': form})

def SetPass(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                login(request, user)
                return redirect('Editor')
            else:
                messages.error(request, 'Las contraseñas no son iguales')
        return render(request, 'setpass.html', {'user_id': user_id})
    except User.DoesNotExist:
        messages.error(request, 'El usuario no existe')


def Editor(request):
    if request.user.is_authenticated:
        name = request.user.username
    else:
        name = None
    return render(request, 'editor.html', {'name': name})

