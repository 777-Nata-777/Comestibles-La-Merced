from django.shortcuts import render

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
    return render(request, 'Productos/index.html')
def empieza (request):
    return render(request, 'empieza.html')
def crear(request):
    return render(request, 'Productos/crear.html')
def editar(request):
    return render(request, 'Productos/editar.html')