from django import forms
from ckeditor.fields import RichTextFormField

class ChatFormulario(forms.Form): 
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    chat = RichTextFormField()
    
class Busquedamensaje(forms.Form):
    nombre = forms.CharField(max_length=20)