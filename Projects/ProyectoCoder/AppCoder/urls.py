from django.contrib import admin
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #URLS
    path("", inicio, name="Inicio"),
    path("buscarJuego/",busquedaJuego,name="BuscarJuego"),
    path("resultados/",resultadosJuego,name="resultados"),
    
    #CRUD profesores 
    path("verJuegos/", leerJuegos, name="JuegosLeer"),
    path("agregarJuegos/", crearJuegos, name="JuegosCrear"),
    path("eliminarJuegos/<juegoNombre>/",eliminarJuegos, name="JuegosEliminar"),
    path("editarJuegos/<juegoNombre>/",editarJuegos, name="JuegosEditar"),
    
    #CRUD cursos con clases
    path("jugadores/list",ListaJugadores.as_view(), name="JugadoresLeer"),
    path("jugadores/<int:pk>",DetalleJugadores.as_view(), name="JugadoresDetalle"),
    path("jugadores/crear", CrearJugadores.as_view(), name = "JugadoresCrear"),
    path("jugadores/editar/<int:pk>",ActualizarJugadores.as_view(), name="JugadoresActualizar"),
    path("jugadores/borrar/<int:pk>",BorrarJugadores.as_view(), name="JugadoresBorrar"),
    path("buscarJugadores/", buscarJugador, name="JugadoresBuscar"),
    path("resultadosJugadores/",resultadosJugador,name="JugadoresResultados"),
    # #CRUD Empresas con clases
     path("empresas/list",ListaEmpresas.as_view(), name="EmpresasLeer"),
     path("empresas/<int:pk>",DetalleEmpresas.as_view(), name="EmpresasDetalle"),
     path("empresas/crear", CrearEmpresas.as_view(), name = "EmpresasCrear"),
     path("empresas/editar/<int:pk>",ActualizarEmpresas.as_view(), name="EmpresasActualizar"),
     path("empresas/borrar/<int:pk>",BorrarEmpresas.as_view(), name="EmpresasBorrar"),
    
    #Iniciar Sesión y registro
    path("login/", iniciarsesion,name="Login"),
    path("register/", registrar,name="Registro"),
    path("logout/",LogoutView.as_view(template_name="AppCoder/logout.html"), name= "Logout"),
    path("editar/", editarUsuario, name="editarUsuario"),
    path("agregarAvatar/", agregarAvatar, name="Avatar"),
    #Acerca de, Contacto
    path("aboutme/", aboutme, name="AcercaDe"),
    path("contact/", contact, name="Contacto"),
]
