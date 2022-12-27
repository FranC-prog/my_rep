from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

# Create your views here.
def inicio(request):
    return HttpResponse("Esta es la vista de bienvenida")
def curso(request):
    
    curso1 = Curso(nombre = "Python", camada = 44775)
    curso1.save()
    return HttpResponse(f"El curso que he creado es {curso1.nombre} y la camada es {curso1.camada}")


