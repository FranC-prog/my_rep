from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Juego(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}"
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length = 400)
    resena = models.CharField(max_length = 700)

class EmpresaDeJuegos(models.Model):
    
    def __str__(self):
        return f"Nombre: {self.nombre}"
    
    nombre = models.CharField(max_length=50)
    juegosDeEmpresa = models.CharField(max_length = 100)
    paisOrigen = models.CharField(max_length=254)
    

class JugadoresProfesionales(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} ---- Tag: {self.tag}"
    
    nombre = models.CharField(max_length=50)
    tag = models.CharField(max_length = 50)
    juego = models.CharField(max_length=50)

    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= "avatares", null = True, blank = True)
    
    

    