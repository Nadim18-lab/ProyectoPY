from django.urls import path
from AppCoder import views

urlpatterns = [
    
    path('Inicio/',views.index),
    path('Receta/',views.receta),
    path('Agregar/',views.agregar),
    path('Editar/',views.editar),
    path('Login/',views.login),
]