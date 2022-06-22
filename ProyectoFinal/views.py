from django.template import loader
from django.http import HttpResponse

def index(request):
    plantilla = loader.get_template("index.html")
    
    documento = plantilla.render()
    return HttpResponse(documento)