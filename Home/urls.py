from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jugadores/', views.ver_jugadores, name='ver_jugadores' ),
    path('jugadores/crear/', views.crear_jugador, name='crear_jugador' ),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros' ),
    path('jugador/ver/<int:pk>', views.VerJugador.as_view(), name='ver_jugador'),
    path('jugadores/editar/<int:pk>', views.Editarjugador.as_view(), name='editar_jugador' ),
    path('jugadores/eliminar/<int:pk>', views.EliminarJugador.as_view(), name='eliminar_jugador' )
]