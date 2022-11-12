from django.shortcuts import render, redirect
from Home.models import Jugador
from Home.forms import Busquedajugador, JugadorFormulario
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
   return render(request, 'Home/index.html') 


   
def ver_jugadores(request):
    
    apellido =  request.GET.get('apellido', None)
    
    if apellido:
        jugadores = Jugador.objects.filter(apellido__icontains=apellido)
    else:
        jugadores = Jugador.objects.all()
    
    formulario = Busquedajugador()
    
    return render(request, 'Home/ver_jugadores.html', {'jugadores': jugadores, 'formulario':formulario})
    
    
@login_required (login_url='/cuenta/login/')
def crear_jugador(request):
    if request.method == 'POST':
        
        formulario = JugadorFormulario(request.POST, request.FILES)        
        
        if formulario.is_valid():
            data = formulario.cleaned_data    
            jugador = Jugador(
                imagen= data['imagen'],
                nombre= data['nombre'],
                apellido= data['apellido'],
                nacionalidad=data['nacionalidad'],
                lugar_de_nacimiento= data['lugar_de_nacimiento'],
                fecha_de_nacimiento= data['fecha_de_nacimiento'],
                edad= data['edad'],
                equipo_actual= data['equipo_actual'],
                posicion= data['posicion'],
                altura= data['altura'],
                peso= data['peso']
            )
            jugador.save()
            
            return redirect('ver_jugadores') 
        else:
            return render(request, 'Home/crear_jugador.html', {'formulario': formulario})
         
    formulario = JugadorFormulario()
        
    return render(request, 'home/crear_jugador.html', {'formulario': formulario})



def sobre_nosotros(request):
   return render(request, 'Home/sobre_nosotros.html')

class VerJugador(DetailView):
    model = Jugador
    template_name = 'Home/ver_jugador.html'
    
class Editarjugador(LoginRequiredMixin, UpdateView):
    model = Jugador
    login_url = '/cuenta/login/'
    success_url = '/jugadores/'
    template_name = 'Home/editar_jugador.html'
    fields = ['imagen',
              'nombre',
              'apellido',
              'nacionalidad',
              'lugar_de_nacimiento',
              'fecha_de_nacimiento',
              'edad',
              'equipo_actual',
              'posicion',
              'altura',
              'peso'
            ]
    
class EliminarJugador(LoginRequiredMixin, DeleteView):
    model = Jugador
    login_url = '/cuenta/login/'
    success_url = '/jugadores/'
    template_name = 'Home/eliminar_jugador.html'