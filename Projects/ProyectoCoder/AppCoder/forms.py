from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    nombre =forms.CharField()
    camada = forms.IntegerField()
    
class ProfeFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    curso = forms.CharField(max_length=50)
    profesion = forms.CharField(max_length=60)

class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = " Repita la contraseña", widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']