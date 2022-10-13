from django.shortcuts import render
from Home.models import Jugador
from Home.forms import JugadorFormulario

def index(request):
   return render(request, 'home/index.html') 
   
def ver_jugadores(request):
    
    jugador = Jugador.objects.all()
    
    return render(request, 'Home/ver_jugadores.html', {'jugador': jugador})
    
    
    
def crear_jugador(request):

    formulario = JugadorFormulario()
    
    return render(request, 'Home/crear_jugador.html', {'formulario': formulario})