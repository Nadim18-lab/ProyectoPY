from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=40)
    tiempo = models.IntegerField()
    ingredientes = models.CharField(max_length=2000)
    pasos = models.CharField(max_length=1000)

class Usuario (models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    contrasena = models.CharField(max_length=40)

class Admin (models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    contrasena = models.CharField(max_length=40)

class Contacto (models.Model):
    motivo = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=1000)