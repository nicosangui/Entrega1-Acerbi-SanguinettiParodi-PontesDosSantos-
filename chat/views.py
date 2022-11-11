from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from chat.forms import ChatFormulario, Busquedamensaje, ResponderMensajeFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import  DeleteView
from chat.models import Chat

@login_required
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
    
def responder_mensaje(request, pk):
    post = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form = ResponderMensajeFormulario(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('ver_mensajes', pk=post.pk)
    else:
        form = ResponderMensajeFormulario()
    return render(request, 'responder_mensajes.html', {'form': form})

