from django import forms
from ckeditor.fields import RichTextFormField

from chat.models import Comentario

class ChatFormulario(forms.Form): 
    chat = RichTextFormField()
    
class Busquedamensaje(forms.Form):
    nombre = forms.CharField(max_length=20)
    
class ResponderMensajeFormulario(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('nombre', 'chat',)