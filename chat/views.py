from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from chat.forms import ChatFormulario, Busquedamensaje, ResponderMensaje
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import  DeleteView
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
    
    usuario =  request.GET.get('usuario', None)
    
    if usuario:
        mensajes = Chat.objects.filter(usuario__icontains=usuario)
    else:
        mensajes = Chat.objects.all()
    
    formulario = Busquedamensaje()
    
    return render(request, 'chat/ver_mensajes.html', {'mensajes': mensajes, 'formulario':formulario})

# @login_required
# def responder_mensaje(request):    
#     if request.method == 'POST':
        
#         formulario = ChatFormulario(request.POST)        
        
#         if formulario.is_valid():
#             data = formulario.cleaned_data    
#             respuesta = Chat(
#                 nombre= data['nombre'],
#                 apellido= data['apellido'],
#                 fecha_de_creacion= datetime.now(),
#                 chat= data['chat'],
#             )
#             respuesta.save()
            
#             return redirect('ver_mensajes') 
#         else:
#             return render(request, 'chat/ver_mensajes.html', {'formulario': formulario})
         
    # formulario = ChatFormulario()
        
    # return render(request, 'chat/escribir_mensaje.html', {'formulario': formulario})
    
    
class EliminarMensaje(LoginRequiredMixin, DeleteView):
    model = Chat
    success_url = '/chat/mensajes/'
    template_name = 'chat/eliminar_mensaje.html'
    
def responder_mensaje(request, pk):
    post = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        formulario = ResponderMensaje(request.POST)
        if formulario.is_valid():
            mensaje = formulario.save(commit=False)
            mensaje.post = post
            mensaje.save()
            return redirect('ver_mensajes', pk=post.pk)
    else:
        formulario = ResponderMensaje()
    return render(request, 'chat/responder_mensaje.html', {'formulario': formulario})

