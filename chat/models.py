from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Chat(models.Model): 
    nombre = models.CharField(max_length=20)
    fecha_de_creacion = models.DateTimeField(auto_now=True)
    chat = RichTextField(null=True)

class Comentario(models.Model):
    nombre = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha_de_creacion = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey(Chat, on_delete=models.PROTECT)
    respuesta = RichTextField(null=True)
