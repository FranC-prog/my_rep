from django.contrib import admin
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #URLS
    path("", inicio, name="Inicio"),
    path("curso/", curso,name="Curso"),
    path("profe/",profesores,name="Profesores"),
    path("estudiante/",estudiantes,name="Estudiantes"),
    path("entregable/",entregables,name="Entregables"),
    path("cursoform/",cursoFormulario,name="FormularioCurso"),
    path("buscarCamada/",busquedaCamada,name="BuscarCamada"),
    path("resultados/",resultados,name="resultados"),
    
    #CRUD profesores 
    path("leerProfes/", leerProfesores, name="ProfesLeer"),
    path("crearProfes/", crearProfesores, name="ProfesCrear"),
    path("eliminarProfes/<profeNombre>/",eliminarProfesores, name="ProfesorEliminar"),
    path("editarProfes/<profeNombre>/",editarProfesores, name="ProfesorEditar"),
    #CRUD cursos con clases
    path("curso/list",ListaCurso.as_view(), name="CursosLeer"),
    path("curso/<int:pk>",DetalleCurso.as_view(), name="CursosDetalle"),
    path("curso/crear", CrearCurso.as_view(), name = "CursosCrear"),
    path("curso/editar/<int:pk>",ActualizarCurso.as_view(), name="CursosActualizar"),
    path("curso/borrar/<int:pk>",BorrarCurso.as_view(), name="CursosBorrar"),
    
    #Iniciar Sesión y registro
    path("login/", iniciarsesion,name="Login"),
    path("register/", registrar,name="Registro"),
    path("logout/",LogoutView.as_view(template_name="AppCoder/logout.html"), name= "Logout")
]