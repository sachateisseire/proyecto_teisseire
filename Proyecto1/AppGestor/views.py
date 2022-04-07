from django.http import HttpResponse
from django.shortcuts import render

from AppGestor.models import Departamentos

# Create your views here.

def departamentos(self):

    departamentos = Departamentos(reparticion="Logistica")
    departamentos.save()

    documentoDeTexto = f'Bien hecho'

    return HttpResponse (documentoDeTexto)
