from django.shortcuts import render, redirect
from Home.models import Jugador
from Home.forms import Busquedajugador, JugadorFormulario
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


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
    
    

def crear_jugador(request):
    if request.method == 'POST':
        
        formulario = JugadorFormulario(request.POST )        
        
        if formulario.is_valid():
            data = formulario.cleaned_data    
            jugador = Jugador(
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
        
    return render(request, 'Home/crear_jugador.html', {'formulario': formulario})



def sobre_nosotros(request):
   return render(request, 'Home/sobre_nosotros.html')

class VerJugador(DetailView):
    model = Jugador
    template_name = 'Home/ver_jugador.html'
    
class Editarjugador(LoginRequiredMixin, UpdateView):
    model = Jugador
    success_url = '/Home/jugadores/'
    template_name = 'Home/editar_jugador.html'
    fields = ['nombre',
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
    success_url = '/Home/jugador/'
    template_name = 'Home/eliminar_jugador.html'