from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import Familiares
from datetime import datetime
# Create your views here.


def inicio(request): 
    return HttpResponse("Ellas son parte integrante de mi familia")

def familiares(request):
     return HttpResponse("Ellas son mis sobrinas ")
