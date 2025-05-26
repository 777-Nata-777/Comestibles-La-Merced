from django.urls import path
from app import views

urlpatterns = [
    path('', views.index,name='inicio'),
    path('Iniciar Sesion', views.iniciar, name='Iniciar Sesion'),
    path('Registrarse', views.registrarse, name='Registrarse'),
]