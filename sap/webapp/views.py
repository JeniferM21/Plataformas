from django.http import HttpResponse
from django.template import loader
from personas.models import Persona
# Create your views here.
def  bienvenida(request):
    #return HttpResponse('<!DOCTYPE HTML><html><head><title> APP </title></head><body><p> Hola mundo </p></body></html>')
    pagina = loader.get_template('saludo.html')
    return HttpResponse(pagina.render())
def hola(request,nombre):
    apellido = request.GET["apellido"]
    nivel = request.GET["nivel"]
    curso = request.GET["curso"]
    pagina = loader.get_template('saludo.html')
    nombreCompleto= nombre+ " " +apellido
    datos={'nombre':  nombreCompleto,'curso':curso,'nivel':nivel}
    return HttpResponse(pagina.render(datos))

def edad(request,edad):
    pagina = loader.get_template('edad.html')
    mensaje={'edad':edad}
    return HttpResponse(pagina.render(mensaje,request))

def mostrar_personas(request):
    cantidad_personas = Persona.objects.count()
    personas= Persona.objects.all().values()    #devuelve una lista de personas

    nombres_personas=list()
    for persona in personas:
         #print(persona)
       nombres_personas.append(persona['nombre'])

    datos= {'cantidad':cantidad_personas,'personas':personas,'nombres_personas': nombres_personas}  #agg un parametro adicional
    pagina=loader.get_template('personas.html')
    return HttpResponse(pagina.render(datos,request))



