from django.urls import path
from chat import views

urlpatterns = [
    path('mensajes/', views.ver_mensajes, name='ver_mensajes' ),
    path('mensajes/escribir/', views.escribir_mensaje, name='escribir_mensaje' ),
    path('mensajes/responder/<int:pk>', views.responder_mensaje, name='responder_mensaje' )
]