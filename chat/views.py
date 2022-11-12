from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from chat.forms import ChatFormulario, Busquedamensaje
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import  DeleteView
from chat.models import Chat

@login_required (login_url='/cuenta/login/')
def escribir_mensaje(request):
    if request.method == 'POST':
        
        formulario = ChatFormulario(request.POST )        
        user = request.user
        if formulario.is_valid():
            data = formulario.cleaned_data    
            mensaje = Chat(
                nombre= user.username,
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
        
class EliminarMensaje(LoginRequiredMixin, DeleteView):
    model = Chat
    success_url = '/chat/mensajes/'
    template_name = 'chat/eliminar_mensaje.html'
    login_url = '/cuenta/login/'
