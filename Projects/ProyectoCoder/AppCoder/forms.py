from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import *

class JugadorFormulario(forms.Form):
    nombre =forms.CharField()
    tag = forms.CharField()
    juego = forms.CharField()
    
class JuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length = 150)
    reseña = forms.CharField(max_length=150)
    
class EmpresaFormulario(forms.Form):
    nombre = models.CharField(max_length=50)
    juegosDeEmpresa = models.CharField(max_length = 100)
    PaisDeOrigen = models.CharField(max_length=254)

class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = " Repita la contraseña", widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        
class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = " Repita la contraseña", widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2']
        
class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["usuario", "imagen"]