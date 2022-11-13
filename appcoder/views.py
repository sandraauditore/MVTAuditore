from django.http import HttpResponse
from django.template import loader
from django.template import  Template, Context
from datetime import datetime
from django.shortcuts import render
from appcoder.models import familiares



def familiares_view(request):

    listaFamiliares = familiares.objects.all()

    fam_dic = {'listaFamiliares': listaFamiliares,}

    plantilla = loader.get_template('appcoder\familiares.html')

    documento = plantilla.render(fam_dic)

    return HttpResponse(documento)

 

     

    