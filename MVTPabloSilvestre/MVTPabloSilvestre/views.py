from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from Home.models import Persona

def crear_familia(request):
    
    persona = Persona(nombre='Pablo', apellido='Silvestre', edad=random.randrange(
        1, 99), fecha_alta=datetime.now())
    persona.save()

    persona = Persona(nombre='Carlos', apellido='Silvestre', edad=random.randrange(
        1, 99), fecha_alta=datetime.now())
    persona.save()

    persona = Persona(nombre='Teresa', apellido='Silvestre', edad=random.randrange(
        1, 99), fecha_alta=datetime.now())
    persona.save()
    
    template = loader.get_template('crear_familia.html')

    template_renderizado = template.render({'personas': persona})

    return(HttpResponse(template_renderizado))
 


def mostrar_familia(request):
    personas = Persona.objects.all()

    template = loader.get_template('ver_familia.html')

    template_renderizado = template.render({'personas': personas})

    return(HttpResponse(template_renderizado))
