from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class ProductoForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ["nombre", "marca", "descripcion", "precio", "stock", "categoria", "imagen","videoid","destacado"]
        

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categorias
        fields = ["nombre"]
        

class MarcaForm(forms.ModelForm):
    
    class Meta:
        model = Marcas
        fields = ["nombre","imagen"]


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = Cliente
        fields = ["username", "first_name","last_name","ape_materno","email","password1","password2","region","provincia","comuna","calle","numero","depto"]
        
class CustomUserCreationFormAdd(UserCreationForm):
    
    class Meta:
        model = Cliente
        fields = ["username", "first_name","last_name","ape_materno","email","password1","password2","region","provincia","comuna","calle","numero","depto","is_staff"]
        
class CustomUserCreationFormListado(UserCreationForm):
    
    class Meta:
        model = Cliente
        fields = ["username", "first_name","last_name","ape_materno","email","password1","password2","region","provincia","comuna","calle","numero","depto"]
        