from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Publicacion
from .forms import PublicacionForm

@login_required
def actualizar(request, publicacion_id):
    publicacion = Publicacion.objects.get(pk=publicacion_id)
    form = PublicacionForm(request.POST or None, instance=publicacion)
    if request.user == publicacion.usuario:
        if form.is_valid():
            form.save()
            messages.success(request, ('Publicacion Acualizada!'))
            return redirect(home)
    else:
        messages.success(request, 'No Eres el dueño de esta publicacion y no puedes actulizarla')
        return redirect('home')
    return render(request, 'app/actualizar.html', {'publicacion':publicacion, 'form':form})

@login_required
def eliminar(request, publicacion_id):
    publicacion = Publicacion.objects.get(pk=publicacion_id)
    if request.user == publicacion.usuario:
        publicacion.delete()
        messages.success(request, ('Publicacion Eliminada!'))
        return redirect(home)
    else:
        messages.success(request, 'No Eres el dueño de esta publicacion y no puedes eliminarla')
        return redirect('home')

@login_required
def agregar(request):
    if request.POST:
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publi = form.save(commit=False)
            publi.usuario = request.user
            publi.save()
            messages.success(request, ('Publicacion Añadida!'))
            return redirect(home)
        
    return render(request, 'app/agregar.html', {'form':PublicacionForm})

@login_required
def home(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'app/home.html', {'publicaciones':publicaciones})