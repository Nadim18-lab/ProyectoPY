from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    plantilla = loader.get_template("index.html")
    
    documento = plantilla.render()
    return HttpResponse(documento)

def receta(request):
    
    return HttpResponse('reloco')


def agregar(request):
    
    return HttpResponse('reloco')


def editar(request):
    
    return HttpResponse('reloco')


def login(request):
    
    return HttpResponse('reloco')


