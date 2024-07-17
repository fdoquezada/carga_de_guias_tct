from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImagenForm
from .models import Imagen
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

@login_required
def subir_imagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            imagen = form.save(commit=False)
            imagen.usuario = request.user
            imagen.save()
            messages.success(request, 'Imagen subida con éxito.')
            return redirect('listar_imagenes')
    else:
        form = ImagenForm()
    return render(request, 'subir_imagen.html', {'form': form})

@login_required
def listar_imagenes(request):
    imagenes = Imagen.objects.filter(usuario=request.user)
    return render(request, 'listar_imagenes.html', {'imagenes': imagenes})

@login_required
def editar_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES, instance=imagen)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagen actualizada con éxito.')
            return redirect('listar_imagenes')
    else:
        form = ImagenForm(instance=imagen)
    return render(request, 'editar_imagen.html', {'form': form, 'imagen': imagen})

@login_required
def eliminar_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk, usuario=request.user)
    if request.method == 'POST':
        imagen.delete()
        messages.success(request, 'Imagen eliminada con éxito.')
        return redirect('listar_imagenes')
    return render(request, 'confirmar_eliminar.html', {'imagen': imagen})

def logout_view(request):
    logout(request)
    return redirect('home')     

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # o cualquier otra página a la que quieras redirigir
        else:
            # Manejar login fallido
            pass
    return render(request, 'login.html')    

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # O cualquier otra página a la que quieras redirigir después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})    