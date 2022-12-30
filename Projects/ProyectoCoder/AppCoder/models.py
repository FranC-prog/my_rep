from django.db import models

# Create your models here.
class Curso(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} --- Camada: {self.camada}"
    
    
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Profesor(models.Model):
    
    def __str__(self):
        return f"Nombre: {self.nombre} --- Curso: {self.curso}"
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    curso = models.CharField(max_length=50)
    profesion = models.CharField(max_length=60)

class Estudiante(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} --- Apellido: {self.apellido}"
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

class Entregable(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} --- Fecha de Entrega: {self.fechaDeEntrega}"
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    