from contextvars import Context
from pipes import Template
from datetime import datetime
from unicodedata import name
from django import http
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader

def saludo(request):
    return HttpResponse('Hola Django Coder')

def probandoTemplate(self):

    nom = 'Nicolas'
    ap = 'Perez'

    diccionario = {'nombre':nom, 'apellido':ap}

    # miHtml = open('C:\\Users\\Oficina\\Desktop\\Entrega1_Teisseire\\Proyecto1\Proyecto1\\plantillas\\template1.html')

    # plantilla = Template(miHtml.read())

    # miHtml.close()

    # miContexto = Context(diccionario)

    # documento = plantilla.render(miContexto)

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
