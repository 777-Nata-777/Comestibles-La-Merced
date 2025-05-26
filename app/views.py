from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "inicio.html")
def iniciar(request):
    return render(request, 'iniciar sesion.html')
def registrarse(request):
    return render(request, 'Registrarse.html')
