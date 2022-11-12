from django import forms

class JugadorFormulario(forms.Form): 
    imagen = forms.ImageField(required = False)
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    nacionalidad = forms.CharField(max_length=20)
    lugar_de_nacimiento = forms.CharField(max_length=20)
    fecha_de_nacimiento = forms.DateField(help_text='MM/DD/AAAA') 
    edad = forms.IntegerField()
    equipo_actual = forms.CharField(max_length=20)
    posicion = forms.CharField(max_length=20)
    altura = forms.DecimalField(decimal_places=2, max_digits=3)
    peso = forms.DecimalField(decimal_places=2, max_digits=5)
    

class Busquedajugador(forms.Form):
    apellido = forms.CharField(max_length=20)