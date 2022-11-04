from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from chat.forms import ChatFormulario, Busquedamensaje
from chat.models import Chat

@login_required
def escribir_mensaje(request):
    if request.method == 'POST':
        
        formulario = ChatFormulario(request.POST )        
        
        if formulario.is_valid():
            data = formulario.cleaned_data    
            mensaje = Chat(
                nombre= data['nombre'],
                apellido= data['apellido'],
                fecha_de_creacion= datetime.now(),
                chat= data['chat'],
            )
            mensaje.save()
            
            return redirect('ver_mensajes') 
        else:
            return render(request, 'chat/ver_mensaje.html', {'formulario': formulario})
         
    formulario = ChatFormulario()
        
    return render(request, 'chat/escribir_mensaje.html', {'formulario': formulario})


def ver_mensajes(request):
    
    nombre =  request.GET.get('nombre', None)
    
    if nombre:
        mensajes = Chat.objects.filter(nombre__icontains=nombre)
    else:
        mensajes = Chat.objects.all()
    
    formulario = Busquedamensaje()
    
    return render(request, 'chat/ver_mensajes.html', {'mensajes': mensajes, 'formulario':formulario})

@login_required
def responder_mensaje(request):
    if request.method == 'POST':
        
        formulario = ChatFormulario(request.POST)        
        
        if formulario.is_valid():
            data = formulario.cleaned_data    
            respuesta = Chat(
                nombre= data['nombre'],
                apellido= data['apellido'],
                fecha_de_creacion= datetime.now(),
                chat= data['chat'],
            )
            respuesta.save()
            
            return redirect('ver_mensajes') 
        else:
            return render(request, 'chat/ver_mensajes.html', {'formulario': formulario})
         
    # formulario = ChatFormulario()
        
    # return render(request, 'chat/escribir_mensaje.html', {'formulario': formulario})

