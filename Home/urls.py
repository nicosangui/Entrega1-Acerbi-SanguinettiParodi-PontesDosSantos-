from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jugadores/', views.ver_jugadores, name='ver_jugadores' ),
    path('jugadores/crear/', views.crear_jugador, name='crear_jugador' ),
]