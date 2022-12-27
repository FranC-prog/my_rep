from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

# Create your views here.
def inicio(request):
    return HttpResponse("Esta es la vista de bienvenida")
def curso(request):
    return HttpResponse("Esta es la vista de los cursos")
def estudiantes(request):
    return HttpResponse("Esta es la vista de los estudiantes")
def profesores(request):
    return HttpResponse("Esta es la vista de los profesores")
def entregables(request):
    return HttpResponse("Esta es la vista de los trabajos entregables")


