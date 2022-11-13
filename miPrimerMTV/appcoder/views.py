from datetime import datetime

from appcoder.models import Familiares
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.



def listadoFamiliares(request):
    
    listadoFamiliares = Familiares.objects.all()

    datos = {'listadoFamiliares': listadoFamiliares}

    plantilla= loader.get_template("coder/familiares.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)
    
    
    
    
    
    
