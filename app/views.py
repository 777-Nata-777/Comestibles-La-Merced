from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    return render(request, 'inicio.html')
def iniciar(request):
    return render(request, 'iniciar sesion.html')
def registrarse(request):
    return render(request, 'Registrarse.html')
def comestibles(request):
    return render(request, 'comestibles.html')
def productos (request):
    productos = producto.objects.all()
    return render(request, 'Productos/index.html', {'productos': productos})
def empieza (request):
    return render(request, 'empieza.html')
def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'Productos/crear.html', {'formulario': formulario})
def editar(request, id):
    producto = productos.objects.get(id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instace=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
    return render(request, 'Productos/editar.html', {'formulario': formulario})
def eliminar(request, id):
    producto = productos.objects.get(id=id)
    producto.delete()
    return render(request, 'Productos')
