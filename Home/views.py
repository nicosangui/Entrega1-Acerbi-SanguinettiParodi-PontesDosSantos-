from django.shortcuts import render
from Home.models import Jugador
from Home.forms import Busquedajugador, JugadorFormulario

def index(request):
   return render(request, 'Home/index.html') 
   
def ver_jugadores(request):
    
    jugador = Jugador.objects.all()
    
    return render(request, 'Home/ver_jugadores.html', {'jugador': jugador})
    
    
def busqueda_jugador(request):
    
    busqueda = Busquedajugador()
    
    return render(request, 'Home/crear_jugador.html', {'busqueda': busqueda})  
        
def crear_jugador(request):
    if request.method == 'POST':
        
        formulario = JugadorFormulario(request.POST )        
        
        if formulario.is_valid():
            data = formulario.cleaned_data    
            nombre = data['nombre']
            apellido = data['apellido']
            nacionalidad = data['nacionalidad']
            lugar_de_nacimiento = data['lugar_de_nacimiento']
            fecha_de_nacimiento = data['fecha_de_nacimiento']
            edad = data['edad']
            equipo_actual = data['equipo_actual']
            posicion = data['posicion']
            altura = data['altura']
            peso = data['peso']
            
            jugador = Jugador(nombre=nombre, apellido=apellido, nacionalidad=nacionalidad, lugar_de_nacimiento=lugar_de_nacimiento, fecha_de_nacimiento=fecha_de_nacimiento, edad=edad, equipo_actual=equipo_actual,posicion=posicion, altura=altura, peso=peso)
            jugador.save()
            
            return redirect('ver_jugadores') 
               
    formulario = JugadorFormulario()
    
    return render(request, 'Home/crear_jugador.html', {'formulario': formulario})