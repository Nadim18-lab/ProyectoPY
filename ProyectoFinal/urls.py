
from django.contrib import admin
from django.urls import path
from ProyectoFinal.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('probando/',index),
]
