from django.http import HttpResponse
from django.template import Template, Context, loader

from datetime import datetime


def vista_saludo(request):
    return HttpResponse('''<h1>Hola Coder!</h1>
    <p style='color:red'  >esto es una prueba' </p>''')

def iniciar_sesion(request):
    return HttpResponse("Pasamae tu username: ")

def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenida {nombre}"
    return HttpResponse(respuesta)

def vista_plantilla(request):
# abrimos archivo
    archivo = open("/Users/Sandra Auditore/Desktop/coder/coderProyecto/miPrimerMTV/miPrimerMTV/templates/plantilla.html")
   # creamos objeto plantilla 
    plantilla = Template(archivo.read())
# cerramos archivo
    archivo.close()

# diccionario con datos para la plantilla

    datos = {"nombre": "Sandra", "fecha": datetime.now(), "apellido": "Auditore", "edad": 55} 




    # creamos el contexto
    contexto = Context(datos)

# renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)
# retornamos la resouesta
    return HttpResponse(documento)
    pass

def vista_listado_familiares(requiest):
   
    #abrimos el archivo
    archivo = open(r"\Users\Sandra Auditore\Desktop\coder\coderProyecto\miPrimerMTV\miPrimerMTV\templates\listado_familiares.html")

    
    # creamos el Tamplete
    plantilla = Template(archivo.read())

# cerramos el archivo
    archivo.close

# creamos el diccionario de los familiares
    listado_familiares = ['Agustina Brusa', 'Valentina Maio', 'Julieta Maio']
    datos = {'familiares': 'Sandra', 'listado_familiares': listado_familiares}

#creamos el contexto
    contexto = Context(datos)

#renderizamos la plantilla para crear la respuesta

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

pass

def vista_listado_familiares2(request):
    listado_familiares = ['Agustina Brusa', 'Valentina Maio', 'Julieta Maio']
    datos = {'familiares': 'Sandra', 'listado_familiares': listado_familiares}


    plantilla = loader.get_template("listado_familiares.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)


    
    
pass