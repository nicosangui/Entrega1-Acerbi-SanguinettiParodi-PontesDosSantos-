from django import forms
from ckeditor.fields import RichTextFormField

from chat.models import Chat

class ChatFormulario(forms.Form): 
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    chat = RichTextFormField()
    
class Busquedamensaje(forms.Form):
    usuario = forms.CharField(max_length=20)
    
class ResponderMensaje(forms.Form):
    class Meta:
        model = Chat
        fields = ('author', 'text',)