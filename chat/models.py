from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Chat(models.Model): 
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_de_creacion = models.DateTimeField(auto_now=True)
    chat = RichTextField(null=True)

