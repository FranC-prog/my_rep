from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")
def curso(request):
    return render(request, "AppCoder/cursos.html")
def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")
def profesores(request):
    return render(request, "AppCoder/profesores.html")
def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
    if request.method == "POST":
        formulario1 = CursoFormulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            curso = Curso(nombre = info["nombre"], camada=info["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = CursoFormulario()
    return render(request,"AppCoder/cursoFormulario.html",{'form1': formulario1})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def resultados(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__iexact = camada)
        return render(request, "AppCoder/inicio.html", {"cursos": cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos."
        
    return HttpResponse(respuesta)

def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {"teachers": profesores}
    return render(request, "AppCoder/leerProfes.html",contexto)

def crearProfesores(request):
    if request.method == "POST":
        formulario1 = ProfeFormulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            profe = Profesor(nombre = info["nombre"], apellido=info["apellido"],email=info["email"], curso=info["curso"], profesion=info["profesion"] )
            profe.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = ProfeFormulario()
    return render(request,"AppCoder/profeFormulario.html",{'profeform': formulario1})

def eliminarProfesores(request, profeNombre):
    profesor = Profesor.objects.get(nombre = profeNombre)
    profesor.delete()
    profesores = Profesor.objects.all()
    contexto = {"teachers": profesores}
    return render(request, "AppCoder/leerProfes.html", contexto)

def editarProfesores(request, profeNombre):
    profesor = Profesor.objects.get(nombre = profeNombre)
    if request.method == "POST":
        formulario1 = ProfeFormulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            profesor.nombre = info["nombre"]
            profesor.apellido = info["apellido"]
            profesor.email = info["email"]
            profesor.curso = info["curso"]
            profesor.profesion = info["profesion"]
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = ProfeFormulario(initial={"nombre" : profesor.nombre, 
                                               "apellido":profesor.apellido,
                                               "email":profesor.email,
                                               "curso":profesor.curso,
                                               "profesion":profesor.profesion})
    return render(request,"AppCoder/editarProfe.html",{'editprofeform': formulario1, 'nombre':profeNombre})
#Vistas del Curso

class ListaCurso(LoginRequiredMixin, ListView):
    model=Curso
class DetalleCurso(LoginRequiredMixin,DetailView):
    model=Curso
class CrearCurso(LoginRequiredMixin, CreateView):
    model=Curso
    success_url="/curso/list"
    fields = ["nombre", "camada"]
class ActualizarCurso(LoginRequiredMixin, UpdateView):
    model=Curso
    success_url="/curso/list"
    fields = ["nombre", "camada"]
class BorrarCurso(LoginRequiredMixin, DeleteView):
    model=Curso
    success_url="/curso/list"
    

def iniciarsesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contra)
            
            if user:
                login(request, user)
                return render(request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido {user}"})
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje": "Los datos son incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {"formulario":form})

def registrar(request):
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html",{"mensaje": "Usuario creado"} )
    else:
        form = UsuarioRegistro()
    return render(request, "AppCoder/registro.html", {"formulario":form})