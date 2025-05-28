from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import producto  # Asumo que el modelo se llama en minúscula
from .forms import ProductoForm

# Vistas generales
def index(request):
    return render(request, 'inicio.html')

def iniciar(request):
    return render(request, 'iniciar sesion.html')

def registrarse(request):
    return render(request, 'Registrarse.html')

def comestibles(request):
    return render(request, 'comestibles.html')

def empieza(request):
    return render(request, 'empieza.html')

# Vista de listado de productos
def productos(request):
    productos_list = producto.objects.all()
    return render(request, 'Productos/index.html', {'productos': productos_list})

# Vista para crear un producto
def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'Productos/crear.html', {'formulario': formulario})

# ✅ Vista corregida para editar
def editar(request, id):
    producto_obj = get_object_or_404(producto, id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto_obj)
    if formulario.is_valid() and request.method == "POST":
        formulario.save()
        return redirect('productos')  # Agregado redirect después de guardar
    return render(request, 'Productos/editar.html', {'formulario': formulario})

# ✅ Vista corregida para eliminar
def eliminar(request, id):
    producto_obj = get_object_or_404(producto, id=id)
    producto_obj.delete()
    return redirect('productos')  # Cambiado render por redirect
