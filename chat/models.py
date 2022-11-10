from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User 
from django.conf import settings


class Chat(models.Model): 
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_de_creacion = models.DateTimeField(auto_now=True)
    chat = RichTextField(null=True)

