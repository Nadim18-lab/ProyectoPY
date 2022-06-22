from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(self):
    plantilla = loader.get_template("index.html")
    
    documento = plantilla.render()
    return HttpResponse(documento)

def receta(self):
    
    return HttpResponse('reloco')


def agregar(self):
    
    return HttpResponse('reloco')


def editar(self):
    
    return HttpResponse('reloco')


def login(self):
    
    return HttpResponse('reloco')


