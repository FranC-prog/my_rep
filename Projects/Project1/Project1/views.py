from django.http import HttpResponse
from django.template import Template, Context,loader
from datetime import datetime

def saludo(request):
    return HttpResponse("Hello World")
def hoy(request):
    fecha = datetime.now()
    return HttpResponse(f"Hoy es: {fecha}.")
def test(request):
    nombre = "Julian"
    pais = "China"
    listaEdades = [1,2,3,4,65,21,12,23,24,25]
    mydict = {"name": nombre, "country": pais, "ages":listaEdades}
    plantilla = loader.get_template("plantilla1.html")
    document = plantilla.render(mydict)
    
    
    return HttpResponse(document)