from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroForm, EmailForm, HistorialForm
from .models import Historial
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroForm, EmailForm, HistorialForm
from .models import Historial


import js2py
from openai import OpenAI

from dotenv import load_dotenv
import os 
load_dotenv()


def Home(request):
    if request.user.is_authenticated:
        return redirect('Editor')
    else:
        return render(request, 'home.html')

def SignUp(request):
    if request.user.is_authenticated:
        return redirect('Editor')
    else:
        if request.method == 'POST':
            form = RegistroForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('Signin')
        else:
            form = RegistroForm()

        return render(request, 'signup.html', {'form': form})

def SignIn(request):
    if request.user.is_authenticated:
        return redirect('Editor')
    else:
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
    
@login_required
def LogOut(request):
    logout(request)
    return redirect('Home')

def ResetPass(request):
    if request.user.is_authenticated:
        return redirect('Editor')
    else:
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
    if request.user.is_authenticated:
        return redirect('Editor')
    else:
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
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('Editor')
    else:
        form = HistorialForm()
    return render(request, 'editor.html', {'form': form})

@login_required
def HistorialList(request):
    Registros = Historial.objects.filter(user=request.user)
    return render(request, 'historial.html', {'registros': Registros})

def Delete(request, registro_id):
    registro = get_object_or_404(Historial, id=registro_id)
    if request.method == 'POST':
        registro.delete()
        return redirect('Historial')
    
    return render(request, 'Historial.html', {'registro': registro})

def Open(request, registro_id):
    registro = get_object_or_404(Historial, id=registro_id)

    if request.method == 'POST':
        form = HistorialForm(request.POST, instance=registro)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('Historial')
    else:
        form = HistorialForm(instance=registro)
    return render(request, 'editor-clon.html', {'registro': registro, 'form': form})

def RenderCode(request):
    def ejecutar_codigo_js(codigo_js):
        try:
            default = execjs.get()
            return default.eval(codigo_js)
            
        except Exception as e:
            return f"Error al ejecutar el código JavaScript: {str(e)}"
    
    code = request.GET.get('code','')
    log = js2py.eval_js("function sumar(){"+code+ "}sumar()")
    
    return HttpResponse( log )

def AnalizeCode(request):
    code = request.GET.get('code','')
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Dame una explicacion para personal no tecnico de que hace este codigo, en caso de que veas un error dimelo"},
        {"role": "user", "content": f"{code}"}
    ]
    )

    reply=completion.choices[0].message.content
    print(reply)
    
    return HttpResponse( reply ) 

    
