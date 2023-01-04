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
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def juegoFormulario(request):
    if request.method == "POST":
        formulario1 = CursoFormulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            curso = Curso(nombre = info["nombre"], camada=info["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = CursoFormulario()
    return render(request,"AppCoder/juegoFormulario.html",{'form1': formulario1})

def busquedaJuego(request):
    return render(request, "AppCoder/busquedaJuego.html")

def resultadosJuego(request):
    if request.GET["nombre"]:
        juego = request.GET["nombre"]
        matches = Juego.objects.filter(juego__icontains = juego)
        return render(request, "AppCoder/inicio.html", {"juegos": matches, "nombre":juego})
    else:
        respuesta = "No enviaste datos."
        
    return HttpResponse(respuesta)

#CRUD JUEGOS/PROFESORES
@login_required
def leerJuegos(request):
    juegos = Juego.objects.all()
    contexto = {"games": juegos}
    return render(request, "AppCoder/leerJuegos.html",contexto)
@login_required
def crearJuegos(request):
    if request.method == "POST":
        formulario1 = JuegoFormulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            juego = Juego(nombre = info["nombre"], descripcion=info["descripcion"], resena=info["resena"])
            juego.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = JuegoFormulario()
    return render(request,"AppCoder/juegoFormulario.html",{'form1': formulario1})


@login_required
def eliminarJuegos(request, juegoNombre):
    juego = Juego.objects.get(nombre = juegoNombre)
    juego.delete()
    juegos = Juego.objects.all()
    contexto = {"games": juegos}
    return render(request, "AppCoder/leerJuegos.html", contexto)
@login_required
def editarJuegos(request, juegoNombre):
    juego = Juego.objects.get(nombre = juegoNombre)
    if request.method == "POST":
        formulario1 = JuegoFormulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            juego.nombre = info["nombre"]
            juego.descripcion = info["descripcion"]
            juego.resena = info["resena"]
            juego.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = JuegoFormulario(initial={"nombre" : juego.nombre, 
                                               "descripcion":juego.descripcion,
                                               "resena":juego.resena,
                                               })
    return render(request,"AppCoder/editarJuego.html",{'editjuegoform': formulario1, 'nombre':profeNombre})


#CRUD CURSO/Jugadores

class ListaJugadores(LoginRequiredMixin, ListView):
    model=JugadoresProfesionales
class DetalleJugadores(LoginRequiredMixin,DetailView):
    model=JugadoresProfesionales
class CrearJugadores(LoginRequiredMixin, CreateView):
    model=JugadoresProfesionales
    success_url="/jugadores/list"
    fields = ["nombre", "tag","juego"]
class ActualizarJugadores(LoginRequiredMixin, UpdateView):
    model=JugadoresProfesionales
    success_url="/jugadores/list"
    fields = ["nombre", "tag","juego"]
class BorrarJugadores(LoginRequiredMixin, DeleteView):
    model=JugadoresProfesionales
    success_url="/jugadores/list"
    
#LOGIN Y USUARIO
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

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        form = FormularioEditar(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.set_password(info["password"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            
            usuario.save()
            return render(request, "AppCoder/inicio.html")
    else:
        form = FormularioEditar(initial={"email":usuario.email,
                                               "first_name":usuario.first_name,
                                               "last_name":usuario.last_name})
    return render(request, "AppCoder/editarPerfil.html", {"formulario": form, "usuario":usuario})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST,request.FILES)
        if form.is_valid():
            usuarioActual = User.objects.get(username = request.user)
            avatar = Avatar(usuario = usuarioActual, imagen = form.cleaned_data["imagen"])
            avatar.save()
            
            return render(request, "AppCoder/inicio.html")
    else:
        form = AvatarFormulario()
    return render(request, "AppCoder/agregarAvatar.html", {"formulario": form})            


#ABOUT ME Y CONTACTO
def aboutme(request):
    return render(request, "AppCoder/acercade.html")

def contact(request):
    return render(request, "AppCoder/contacto.html")

#CRUD EMPRESAS CON CLASES
class ListaEmpresas(LoginRequiredMixin, ListView):
    model=EmpresaDeJuegos
class DetalleEmpresas(LoginRequiredMixin,DetailView):
    model=EmpresaDeJuegos
class CrearEmpresas(LoginRequiredMixin, CreateView):
    model=EmpresaDeJuegos
    success_url="/empresas/list"
    fields = ["nombre", "juegosDeEmpresa","paisOrigen"]
class ActualizarEmpresas(LoginRequiredMixin, UpdateView):
    model=EmpresaDeJuegos
    success_url="/empresas/list"
    fields = ["nombre", "juegosDeEmpresa","paisOrigen"]
class BorrarEmpresas(LoginRequiredMixin, DeleteView):
    model=EmpresaDeJuegos
    success_url="/empresas/list"



        